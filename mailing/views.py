from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DetailView, DeleteView
from django.core.cache import cache
from blog.models import Blog
from clients.models import Client
from config.services import UserPassThroughTestMixin
from .apps import MailingConfig
from mailing.models import Mailing
from django.urls import reverse_lazy
from datetime import datetime
from pytz import timezone
import random
from config.settings import TIME_ZONE, TOPIC_TUPLE, CACHE_ENABLED
from .forms import MailingForm, MailingFormUpdate

# Create your views here.
topic_name = MailingConfig.name


def get_index(request):
    """Главная страница показывающая количество блогов в quantity_objects"""
    template_name = f'{topic_name}/index.html'
    quantity_objects = 3
    #  Часть кода по кеширования объекта quantity_mailing
    if CACHE_ENABLED:
        quantity_mailing = cache.get('quantity_mailing')
        if quantity_mailing is None:
            quantity_mailing = Mailing.objects.count()
            cache.set('quantity_mailing', quantity_mailing, 60 * 1)  # 1 minute
    else:
        quantity_mailing = Mailing.objects.count()
    #  Часть кода по кеширования объекта quantity_active_mailing
    if CACHE_ENABLED:
        quantity_active_mailing = cache.get('quantity_active_mailing')
        if quantity_active_mailing is None:
            quantity_active_mailing = Mailing.objects.filter(is_active=True).count()
            cache.set('quantity_active_mailing', quantity_active_mailing, 60 * 1)  # 1 minute
    else:
        quantity_active_mailing = Mailing.objects.filter(is_active=True).count()
    #  Сначала берем всех Queryset, потом превращаем в словарь, т.к. с ним работать быстрее из-за хеширования
    #  затем создаем множество из 'email' объектов
    if CACHE_ENABLED:
        all_clients_dict = cache.get('all_clients_dict')
        if all_clients_dict is None:
            all_clients_dict = Client.objects.all().values()
            cache.set('all_clients_dict', all_clients_dict, 60 * 1)  # 1 minute
    else:
        all_clients_dict = Client.objects.all().values()
    count_clients = len({element['email'] for element in all_clients_dict})
    #  Далее идет блок формирования рандомных статей в кол-ве равном quantity_objects
    lst = list(Blog.objects.all())
    random.shuffle(lst)
    sliced_lst = lst[:quantity_objects]
    for blog in sliced_lst:
        blog.count_view += 1
        blog.save()
    return render(request, template_name, {'blogs': sliced_lst, 'quantity_mailing': quantity_mailing,
                    'quantity_active_mailing': quantity_active_mailing, 'count_clients': count_clients})


class MailingListView(LoginRequiredMixin, ListView):
    """Представление списка рассылок"""
    model = Mailing
    paginate_by = 4
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }
    context_object_name = 'mailing'

    def get_queryset(self):
        """Возвращает список из объектов QUERYSET по условиям ниже"""
        queryset = super().get_queryset()
        # Блок проверки прав, если пользователь имеет права группы managers, то получает все объекты Client
        # иначе получает только те, которые принадлежат текущему пользователю
        try:
            #  Если пользователь - superuser, то он и так должен видеть всех клиентов, если входит в группу managers,
            # то он должен видеть тоже всех клиентов, иначе(падает в ошибку) - только собственных клиентов
            if self.request.user.is_superuser or self.request.user.groups.get(name='managers'):
                return queryset
        except ObjectDoesNotExist:
            return queryset.filter(owner=self.request.user)  # список всех клиентов созданных юзером


class MailingCreateView(LoginRequiredMixin, CreateView):
    """Представление создания рассылок"""
    model = Mailing
    form_class = MailingForm
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        if form.is_valid():
            client = form.save()
            client.owner = self.request.user
            client.save()
            return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = Mailing(owner=self.request.user)
        return kwargs


class MailingUpdateView(LoginRequiredMixin, UserPassThroughTestMixin, UpdateView):
    """Логика прав находится в кастомном миксине UserPassThroughTestMixin из-за DRY
    Логика формы поменялась, чтобы даты не обнулялись каждый раз"""
    model = Mailing
    form_class = MailingFormUpdate
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        """ Метод для определения статуса 'в ожидании', если текущая дата попытки меньше даты порога и дата
        порога больше даты и времени текущего момента"""
        now = datetime.now(timezone(TIME_ZONE))  # Временная зон
        if form.is_valid():
            if (self.get_object().date_time_attempt < self.get_object().date_time_threshold and
                    self.get_object().date_time_threshold > now):
                mail = form.save()
                mail.status = 'В ожидании'
                mail.save()
        return super().form_valid(form)


class MailingDetailView(LoginRequiredMixin, DetailView):
    """Здесь логика проверки прав пользователей прописана иначе, чем в MailingUpdateView и MailingDeleteView"""
    model = Mailing
    form_class = MailingForm
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }

    def get_object(self, queryset=None):
        """Метод получения объекта исходя из того, что перед ним: создатель, суперюзер или участник группы менеджеров"""
        mail = super().get_object()
        try:
            if self.request.user.is_superuser or self.request.user == mail.owner or self.request.user.groups.get(
                    name='managers'):
                return mail
        except ObjectDoesNotExist:
            raise PermissionDenied('У вас нет доступа к этому сообщению.')


class MailingDeleteView(LoginRequiredMixin, UserPassThroughTestMixin, DeleteView):
    """Представление удаления рассылки"""
    model = Mailing
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }
    success_url = reverse_lazy('mailing:mailing_list')


def toggle_activity(request, pk):
    """Функция для переключения статусов рассылок"""
    mailing = get_object_or_404(Mailing, pk=pk)
    if mailing.is_active:
        mailing.is_active = False
    else:
        mailing.is_active = True
    mailing.save()
    return redirect(reverse_lazy('mailing:mailing_list'))
