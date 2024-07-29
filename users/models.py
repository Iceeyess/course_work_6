from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
NULLABLE = dict(null=True, blank=True)


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Электронная почта', help_text='Введите электронную почту')
    user_image = models.ImageField(upload_to='users/', **NULLABLE)
    is_active = models.BooleanField(verbose_name='Статус пользователя')
    token = models.CharField(max_length=100, verbose_name='Токен', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def __repr__(self):
        return self.email

    def __str__(self):
        return self.email