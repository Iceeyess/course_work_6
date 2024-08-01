from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DetailView, DeleteView

from config.services import UserPassThroughTestMixin
from .apps import MailingConfig
from mailing.models import Mailing
from django.urls import reverse_lazy
from datetime import datetime
from pytz import timezone
from config.settings import TIME_ZONE, TOPIC_TUPLE
from .forms import MailingForm

# Create your views here.
topic_name = MailingConfig.name


class MainTemplateView(TemplateView):
    """Главная страница"""
    template_name = f'{topic_name}/index.html'


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    paginate_by = 4
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }

    def get_queryset(self):
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
    model = Mailing
    form_class = MailingForm
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        now = datetime.now(timezone(TIME_ZONE))  # Временная зон
        if form.is_valid():
            if (self.get_object().date_time_attempt < self.get_object().date_time_threshold and
                    self.get_object().date_time_threshold > now):
                mail = form.save()
                mail.status = 'В ожидании'
                mail.save()
        return super().form_valid(form)


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    form_class = MailingForm
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }

    def get_object(self, queryset=None):
        mail = super().get_object()
        try:
            if self.request.user.is_superuser or self.request.user.groups.get(name='managers'):
                return mail
        except ObjectDoesNotExist:
            raise PermissionDenied('У вас нет доступа к этому сообщению.')


class MailingDeleteView(LoginRequiredMixin, UserPassThroughTestMixin, DeleteView):
    model = Mailing
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }
    success_url = reverse_lazy('mailing:mailing_list')


def toggle_activity(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)
    if mailing.is_active:
        mailing.is_active = False
    else:
        mailing.is_active = True
    mailing.save()
    return redirect(reverse_lazy('mailing:mailing_list'))