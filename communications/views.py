from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from communications.apps import CommunicationsConfig
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy

from communications.forms import CommunicationForm
from communications.models import Communication
from config.settings import TOPIC_TUPLE

# Create your views here.
topic_name = CommunicationsConfig.name


class CommunicationListView(LoginRequiredMixin, ListView):
    model = Communication
    paginate_by = 4
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }


class CommunicationCreateView(LoginRequiredMixin, CreateView):
    model = Communication
    form_class = CommunicationForm
    success_url = reverse_lazy('communications:communication_list')
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }

    def form_valid(self, form):
        if form.is_valid():
            client = form.save()
            client.owner = self.request.user
            client.save()
            return super().form_valid(form)

class CommunicationUpdateView(LoginRequiredMixin, UpdateView):
    model = Communication
    form_class = CommunicationForm
    success_url = reverse_lazy('communications:communication_list')
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }


class CommunicationDetailView(LoginRequiredMixin, DetailView):
    model = Communication
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }


class CommunicationDeleteView(LoginRequiredMixin, DeleteView):
    model = Communication
    success_url = reverse_lazy('communications:communication_list')
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }
