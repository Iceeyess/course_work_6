from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Client(models.Model):
    email = models.EmailField(verbose_name='Электронная почта', help_text='Введите электронную почту')
    full_name = models.CharField(max_length=100, verbose_name='Ф.И.О.', help_text='Введите Ф.И.О.')
    comment = models.TextField(verbose_name='Комментарий', help_text='Введите комментарий')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Mailing(models.Model):
    date_time_first_try = models.DateTimeField()
