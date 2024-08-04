from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from config.services import UserPassThroughTestMixin  #  кастомный переопределенный класс
from config.settings import TOPIC_TUPLE
from .apps import ClientsConfig
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from clients.models import Client
from django.urls import reverse_lazy

from .forms import ClientForm
from django.contrib.auth.models import Permission, Group

# Create your views here.
topic_name = ClientsConfig.name


class ClientListView(LoginRequiredMixin, ListView):
    """Список клиентов"""
    model = Client
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


class ClientCreateView(LoginRequiredMixin, CreateView):
    """Создание клиента"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('clients:client_list')
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }

    def form_valid(self, form):
        """Сохраняем №  пользователя в ID клиента"""
        if form.is_valid():
            client = form.save()
            client.owner = self.request.user
            client.save()
            return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UserPassThroughTestMixin, UpdateView):
    """Редактирование клиента"""
    model = Client
    success_url = reverse_lazy('clients:client_list')
    form_class = ClientForm

    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }

    def test_func(self):
        # Если пользователь - superuser или создатель клиента, то может редактировать клиента
        # Менеджеры такими полномочиями не наделены
        owner = self.get_object().owner
        return self.request.user.is_superuser or self.request.user == owner


class ClientDetailView(LoginRequiredMixin, UserPassThroughTestMixin, DetailView):
    """Детализация клиента"""
    model = Client
    form_class = ClientForm
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }


class ClientDeleteView(LoginRequiredMixin, UserPassThroughTestMixin, DeleteView):
    """Удаление клиента"""
    model = Client
    success_url = reverse_lazy('clients:client_list')
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }

    def test_func(self):
        # Если юзер - superuser или создатель клиента, то может удалить клиента, менеджеры не могу удалять клиентов.
        owner = self.get_object().owner
        return self.request.user.is_superuser or self.request.user == owner

