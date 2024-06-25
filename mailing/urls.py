from django.urls import path
from .apps import MailingConfig
from mailing.views import MainTemplateView, MailingListView

app_name = MailingConfig.name


urlpatterns = [
    path('', MainTemplateView.as_view(), name='main_page'),
    path('mailing/', MailingListView.as_view(), name='mailing_list'),
]
