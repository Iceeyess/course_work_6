from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render

from config.settings import TOPIC_TUPLE
from .apps import ClientsConfig
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from clients.models import Client
from django.urls import reverse_lazy

from .forms import ClientForm

# Create your views here.
topic_name = ClientsConfig.name


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic_name'] = topic_name  # Для возврата в меню
        context['TOPIC_TUPLE'] = TOPIC_TUPLE  # Для визуального переключения разделов в шаблоне
        context['clients_list'] = Client.objects.filter(owner=self.request.user) # список всех клиентов созданных юзером
        return context


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('clients:client_list')
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }

    def form_valid(self, form):
        if form.is_valid():
            client = form.save()
            client.owner = self.request.user
            client.save()
            return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    success_url = reverse_lazy('clients:client_list')
    form_class = ClientForm

    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }
    permission_required = 'clients.change_client'


class ClientDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Client
    form_class = ClientForm
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }
    permission_required = 'clients.view_client'


class ClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('clients:client_list')
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }
    permission_required = 'clients.delete_client'
