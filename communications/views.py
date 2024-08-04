from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from communications.apps import CommunicationsConfig
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy

from communications.forms import CommunicationForm
from communications.models import Communication
from config.services import UserPassThroughTestMixin
from config.settings import TOPIC_TUPLE

# Create your views here.
topic_name = CommunicationsConfig.name


class CommunicationListView(LoginRequiredMixin, ListView):
    """Список сообщений"""
    model = Communication
    paginate_by = 4
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }

    def get_queryset(self):
        """Возвращает список объектов QUERYSET по нижеуказанным условиям"""
        queryset = super().get_queryset()
        # Блок проверки прав, если пользователь имеет права группы managers, то получает все объекты Communication
        # иначе получает только те, которые принадлежат текущему пользователю
        try:
            #  Если пользователь - superuser, то он и так должен видеть все Сообщения, если входит в группу managers,
            # то он должен видеть тоже все сообщения, иначе(падает в ошибку) - только собственные сообщения
            if self.request.user.is_superuser or self.request.user.groups.get(name='managers'):
                return queryset
        except ObjectDoesNotExist:
            return queryset.filter(owner=self.request.user)  # список всех клиентов созданных юзером


class CommunicationCreateView(LoginRequiredMixin, CreateView):
    """Класс создания сообщения"""
    model = Communication
    form_class = CommunicationForm
    success_url = reverse_lazy('communications:communication_list')
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }

    def form_valid(self, form):
        """Форма действительна, то сохраняет номер пользователя в поле owner, чтобы в последствии при создании
        рассылок, можно было читать только собственные сообщения"""
        if form.is_valid():
            client = form.save()
            client.owner = self.request.user
            client.save()
            return super().form_valid(form)


class CommunicationUpdateView(LoginRequiredMixin, UserPassThroughTestMixin, UpdateView):
    """Класс редактирования сообщения"""
    model = Communication
    form_class = CommunicationForm
    success_url = reverse_lazy('communications:communication_list')
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }


class CommunicationDetailView(LoginRequiredMixin, UserPassThroughTestMixin, DetailView):
    """Класс чтения сообщения"""
    model = Communication
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }


class CommunicationDeleteView(UserPassThroughTestMixin, DeleteView):
    """"Класс удаления сообщения"""
    model = Communication
    success_url = reverse_lazy('communications:communication_list')
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }

