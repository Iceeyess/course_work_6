from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config.settings import TOPIC_TUPLE
from users.apps import UsersConfig
from users.forms import UserLoginForm, UserRegistrationForm
from users.models import User

topic_name = UsersConfig.name
# Create your views here


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    extra_context = {
        'topic_name': topic_name,
        'TOPIC_TUPLE': TOPIC_TUPLE
    }


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    extra_context = {
        'topic_name': topic_name,
        'TOPIC_TUPLE': TOPIC_TUPLE
    }
    success_url = reverse_lazy('users:login')