from django.urls import path
from .apps import CommunicationsConfig
from communications.views import (CommunicationListView, CommunicationCreateView, CommunicationUpdateView,
                                  CommunicationDetailView, CommunicationDeleteView)

app_name = CommunicationsConfig.name

urlpatterns = [
    path('', CommunicationListView.as_view(), name='communication_list'),
    path('create/', CommunicationCreateView.as_view(), name='communication_create'),
    path('edit/<int:pk>/', CommunicationUpdateView.as_view(), name='communication_update'),
    path('detail/<int:pk>/', CommunicationDetailView.as_view(), name='communication_detail'),
    path('delete/<int:pk>/', CommunicationDeleteView.as_view(), name='communication_delete'),
]