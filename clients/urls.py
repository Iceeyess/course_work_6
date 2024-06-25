from django.urls import path
from .apps import ClientsConfig
from clients.views import ClientListView, ClientCreateView

app_name = ClientsConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('create/', ClientCreateView.as_view(), name='client_create'),
    path('edit/<int:pk>/', ClientCreateView.as_view(), name='client_update'),
]
