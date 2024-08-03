from django.urls import path
from .apps import MailingConfig
from mailing.views import (get_index, MailingListView, MailingCreateView, MailingDetailView, MailingUpdateView,
                           MailingDeleteView, toggle_activity)

app_name = MailingConfig.name

urlpatterns = [
    path('', get_index, name='main_page'),
    path('list/', MailingListView.as_view(), name='mailing_list'),
    path('create/', MailingCreateView.as_view(), name='mailing_create'),
    path('detail/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('edit/<int:pk>/', MailingUpdateView.as_view(), name='mailing_update'),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),
]
