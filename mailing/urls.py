from django.urls import path
from .apps import MailingConfig
from mailing.views import MainTemplateView, MailingListView, MailingCreateView

app_name = MailingConfig.name


urlpatterns = [
    path('', MainTemplateView.as_view(), name='main_page'),
    path('list/', MailingListView.as_view(), name='mailing_list'),
    path('create/', MailingCreateView.as_view(), name='mailing_create'),
]
