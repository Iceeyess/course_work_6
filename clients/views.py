from django.shortcuts import render
from .apps import ClientsConfig
from django.views.generic import ListView, CreateView, UpdateView
from clients.models import Client
from django.urls import reverse_lazy

# Create your views here.
topic_name = ClientsConfig.name


class ClientListView(ListView):
    model = Client
    paginate_by = 4


class ClientCreateView(CreateView):
    model = Client
    fields = ('email', 'full_name', 'comment', )
    success_url = f'/{topic_name}/'


class ClientUpdateView(UpdateView):
    model = Client
    success_url = reverse_lazy(f'/{topic_name}/')
