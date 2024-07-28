from django.contrib.auth.views import LogoutView
from django.urls import path
from .apps import UsersConfig
from . import views


app_name = UsersConfig.name

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.UserRegisterView.as_view(), name='register')
]
