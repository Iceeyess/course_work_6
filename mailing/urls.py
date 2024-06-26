from django.urls import path
from .apps import MailingConfig
from mailing.views import MainTemplateView, MailingListView, MailingCreateView, MailingDetailView, MailingUpdateView, MailingDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('', MainTemplateView.as_view(), name='main_page'),
    path('list/', MailingListView.as_view(), name='mailing_list'),
    path('create/', MailingCreateView.as_view(), name='mailing_create'),
    path('detail/<int:id>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('edit/<int:id>/', MailingUpdateView.as_view(), name='mailing_update'),
    path('delete/<int:id>/', MailingDeleteView.as_view(), name='mailing_delete'),
]
