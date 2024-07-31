from django.db import models

from users.models import User


# Create your models here.
NULLABLE = dict(blank=True, null=True)

class Client(models.Model):
    email = models.EmailField(verbose_name='Электронная почта', help_text='Введите электронную почту')
    full_name = models.CharField(max_length=100, verbose_name='Ф.И.О.', help_text='Введите Ф.И.О.')
    comment = models.TextField(verbose_name='Комментарий', help_text='Введите комментарий')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец записи', **NULLABLE)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('pk', )
