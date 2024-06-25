from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .apps import MailingConfig
from mailing.models import Mailing

# Create your views here.
topic_name = MailingConfig.name


class MainTemplateView(TemplateView):
    template_name = f'{topic_name}/index.html'


class MailingListView(ListView):
    model = Mailing



