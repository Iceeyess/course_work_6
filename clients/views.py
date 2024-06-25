from django.shortcuts import render
from .apps import ClientsConfig
from django.views.generic import ListView, CreateView
from clients.models import Client

# Create your views here.
topic_name = ClientsConfig.name


class ClientListView(ListView):
    model = Client
    paginate_by = 4


class ClientCreateView(CreateView):
    model = Client
    fields = ('email', 'full_name', 'comment', )
