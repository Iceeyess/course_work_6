from django.shortcuts import render
from communications.apps import CommunicationsConfig
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from communications.models import Communication

# Create your views here.
topic_name = CommunicationsConfig.name


class CommunicationListView(ListView):
    model = Communication
    paginate_by = 4
    extra_context = {'title': topic_name}


class CommunicationCreateView(CreateView):
    model = Communication
    fields = '__all__'
    success_url = reverse_lazy('communications:communication_list')
    extra_context = {'topic_name': topic_name}  # Для возврата


class CommunicationUpdateView(UpdateView):
    model = Communication
    fields = '__all__'
    success_url = reverse_lazy('communications:communication_list')


extra_context = {'topic_name': topic_name}  # Для возврата


class CommunicationDetailView(DetailView):
    model = Communication
    extra_context = {'topic_name': topic_name}  # Для возврата


class CommunicationDeleteView(DeleteView):
    model = Communication
    success_url = reverse_lazy('communications:communication_list')
    extra_context = {'topic_name': topic_name}  # Для возврата
