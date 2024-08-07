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
    path('manage/', views.UsersList.as_view(), name='users_list'),
    path('manage/<int:pk>', views.manage_user_status, name='user_manage'),
    path('registration-email-confirm/<str:token>/', email_verification, name='email-confirm'),
    # Восстановление пароля:
    path('password_reset/', PasswordResetView.as_view(template_name='users/password_reset_form.html',
                                                      email_template_name='users/password_reset_email.html',
                                                      success_url=reverse_lazy('users:password_reset_done')),
         name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    # path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
    #     template_name='users/password_reset_confirm.html', success_url=reverse_lazy('users:password_reset_complete')),
    #      name='password_reset_confirm'),
    path('password_reset/<uidb64>/<token>/', views.UserPasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'), name='password_reset_complete'),

]
