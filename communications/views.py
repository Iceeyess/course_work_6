from django.shortcuts import render
from communications.apps import CommunicationsConfig
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from communications.models import Communication
from config.settings import TOPIC_TUPLE

# Create your views here.
topic_name = CommunicationsConfig.name


class CommunicationListView(ListView):
    model = Communication
    paginate_by = 4
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }


class CommunicationCreateView(CreateView):
    model = Communication
    fields = '__all__'
    success_url = reverse_lazy('communications:communication_list')
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }


class CommunicationUpdateView(UpdateView):
    model = Communication
    fields = '__all__'
    success_url = reverse_lazy('communications:communication_list')
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }


class CommunicationDetailView(DetailView):
    model = Communication
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }


class CommunicationDeleteView(DeleteView):
    model = Communication
    success_url = reverse_lazy('communications:communication_list')
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }
