from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from config.settings import TOPIC_TUPLE
from users.apps import UsersConfig
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User

import secrets

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

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.token = secrets.token_hex(16)



class UserProfileView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    extra_context = {
        'topic_name': topic_name,
        'TOPIC_TUPLE': TOPIC_TUPLE
    }

    def get_success_url(self):
        return reverse_lazy('mailing:mailing_list')
