from django.shortcuts import render
from .apps import ClientsConfig
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from clients.models import Client
from django.urls import reverse_lazy

# Create your views here.
topic_name = ClientsConfig.name


# class ClientLink:
#     extra_context = {'title': topic_name}


class ClientListView(ListView):
    model = Client
    paginate_by = 4
    extra_context = {'title': topic_name}


class ClientCreateView(CreateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('clients:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    success_url = reverse_lazy(f'{topic_name}/')
    fields = '__all__'


class ClientDetailView(DetailView):
    model = Client
    fields = '__all__'


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('clients:client_list')