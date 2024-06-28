from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView
from .apps import MailingConfig
from mailing.models import Mailing

# Create your views here.
topic_name = MailingConfig.name


class MainTemplateView(TemplateView):
    template_name = f'{topic_name}/index.html'


class MailingListView(ListView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    fields = ('date_time_first_try', 'period', 'message', 'client', )
    extra_context = {'topic_name': topic_name}  # Для возврата


