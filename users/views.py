from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordResetConfirmView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView

from config.services import send_registration_email, IsUserManagerOrSuperUser
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
        host = self.request.get_host()
        user.save()
        url = f'http://{host}/users/registration-email-confirm/{user.token}/'
        send_registration_email(form.cleaned_data, url)
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    if user:
        user.is_active = True
        user.save()
        return redirect(reverse('users:login'))


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


class UserPasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uidb64'] = self.kwargs.get('uidb64')
        context['token'] = self.kwargs.get('token')
        return context


class UsersList(LoginRequiredMixin, IsUserManagerOrSuperUser, ListView):
    model = User
    form_class = UserProfileForm
    paginate_by = 20
    extra_context = {
        'topic_name': topic_name,
        'TOPIC_TUPLE': TOPIC_TUPLE
    }


def manage_user_status(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user.pk == request.user.pk:
        return redirect(reverse('users:users_list'))
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    return redirect(reverse('users:users_list'))

