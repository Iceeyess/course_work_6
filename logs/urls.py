from django.urls import path
from .apps import LogsConfig
from . import views

app_name = LogsConfig.name

urlpatterns = [
    path('', views.LogsListView.as_view(), name='logs_list'),
]