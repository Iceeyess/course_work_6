from django.shortcuts import render

from config.settings import TOPIC_TUPLE
from .apps import ClientsConfig
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from clients.models import Client
from django.urls import reverse_lazy

# Create your views here.
topic_name = ClientsConfig.name


class ClientListView(ListView):
    model = Client
    paginate_by = 4
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }


class ClientCreateView(CreateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('clients:client_list')
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }


class ClientUpdateView(UpdateView):
    model = Client
    success_url = reverse_lazy('clients:client_list')
    fields = '__all__'
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }


class ClientDetailView(DetailView):
    model = Client
    fields = '__all__'
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('clients:client_list')
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }
