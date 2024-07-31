from django.contrib.auth.mixins import LoginRequiredMixin
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
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }


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


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    success_url = reverse_lazy('clients:client_list')
    form_class = ClientForm

    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    form_class = ClientForm
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('clients:client_list')
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }
