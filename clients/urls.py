from django.urls import path
from .apps import ClientsConfig
from clients.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDetailView, ClientDeleteView

app_name = ClientsConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('create/', ClientCreateView.as_view(), name='client_create'),
    path('edit/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
]
