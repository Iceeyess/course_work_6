from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path, reverse_lazy
from .apps import UsersConfig
from . import views
from .views import email_verification

app_name = UsersConfig.name

urlpatterns = [
    path('', views.UserLoginView.as_view(), name='login'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', views.UserProfileView.as_view(), name='profile'),
    path('registration-email-confirm/<str:token>/', email_verification, name='email-confirm'),
    # Восстановление пароля:
    path('password-reset/', PasswordResetView.as_view(template_name='users/password-reset-form.html',
                                                      email_template_name='users/password-reset-email.html',
                                                      success_url=reverse_lazy('users:password_reset_done')),
         name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password-reset-done.html'),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='users/password-reset-confirm.html', success_url=reverse_lazy('users:password_reset_confirm')),
         name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(
        template_name='users/password-reset-complete.html'), name='password_reset_complete'),

]
