from django.db import models
from clients.models import Client
from communications.models import Communication
from datetime import datetime
from pytz import timezone
from config.settings import TIME_ZONE

NULLABLE = dict(null=True, blank=True)


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
    date_time_last_attempt = models.DateTimeField(default=datetime.now(timezone(TIME_ZONE)), verbose_name='Дата '
                                                                                        'и время последней попытки')
    status = models.CharField(default="Не отправлялось", max_length=50, verbose_name='Статус рассылки')
    server_code_response = models.IntegerField(verbose_name='Номер рассылки', **NULLABLE, )
    server_response = models.CharField(max_length=3000, verbose_name='Ответ от сервера', **NULLABLE, )


    def __str__(self):
        return self.server_answer

    class Meta:
        verbose_name = 'статус рассылки'
        verbose_name_plural = 'статусы рассылок'


class Mailing(models.Model):
    date_time_attempt = models.DateTimeField(default=datetime.now(), verbose_name='Дата и время первой рассылки',
                                             help_text='Введите дату и время первой рассылки. По умолчанию - текущее время')
    date_time_threshold = models.DateTimeField(default=datetime.now(), verbose_name='Дата и время окончания периода',
                                               help_text='Введите дату и время окончания рассылок. По умолчанию - текущее время')
    period = models.ForeignKey(Frequency, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='В ожидании')
    message = models.ForeignKey(Communication, on_delete=models.CASCADE)
    client = models.ManyToManyField(Client, related_name='mailings')
    log = models.ForeignKey(Log, on_delete=models.SET_NULL, **NULLABLE, db_constraint=False)

    def __str__(self):
        return (f'Дата попытки последней рассылки{self.date_time_attempt}, дата и время окончания рассылки '
                f'{self.date_time_threshold}')

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('pk',)
