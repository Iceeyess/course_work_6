from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from logs.apps import LogsConfig
from logs.models import Log
from config.settings import TOPIC_TUPLE

topic_name = LogsConfig.name

# Create your views here.


class LogsListView(LoginRequiredMixin, ListView):
    model = Log
    paginate_by = 4
    extra_context = {
        'topic_name': topic_name,
        'TOPIC_TUPLE': TOPIC_TUPLE
    }