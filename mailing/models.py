from django.db import models
from clients.models import Client
from communications.models import Communication
from datetime import datetime

# Create your models here.


class Frequency(models.Model):
    # Frequency - частота (периодичность) рассылки
    period = models.CharField(verbose_name='Период', help_text='Введите период')

    def __str__(self):
        return self.period

    class Meta:
        verbose_name = 'период'
        verbose_name_plural = 'периоды'


class Log(models.Model):
    date_time_last_try = models.DateField(default='1900-01-01', verbose_name='Дата и время последней попытки рассылки')
    status = models.CharField(default="Не отправлялось", max_length=50, verbose_name='Статус рассылки')
    server_answer = models.CharField(default=None, max_length=100, verbose_name='Ответ от сервера')

    def __str__(self):
        return self.server_answer

    class Meta:
        verbose_name = 'статус рассылки'
        verbose_name_plural = 'статусы рассылок'


class Mailing(models.Model):
    date_time_first_try = models.DateTimeField(default=datetime.now(), verbose_name='Дата и время первой рассылки',
                                               help_text='Введите дату и время первой рассылки. По умолчанию - текущее время')
    date_time_threshold = models.DateTimeField(default=datetime.now(), verbose_name='Дата и время окончания периода',
                                               help_text='Введите дату и время окончания рассылок. По умолчанию - текущее время')
    period = models.ForeignKey(Frequency, on_delete=models.CASCADE)
    status = models.ForeignKey(Log, on_delete=models.CASCADE, blank=True, null=True)
    message = models.ForeignKey(Communication, on_delete=models.CASCADE)
    client = models.ManyToManyField(Client, related_name='mailings')

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('pk', )
