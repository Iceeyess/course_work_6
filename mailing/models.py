from django.db import models
from clients.models import Client
from communications.models import Communication
from datetime import datetime
from pytz import timezone
from config.settings import TIME_ZONE
from users.models import User

# Create your models here.
NULLABLE = dict(null=True, blank=True)


class Mailing(models.Model):
    # period_choices = (86400, 'Раз в день'), (604800, 'Раз в неделю'), (2592000, 'Раз в месяц',)
    period_choices = (60, 'Раз в минуту'), (60 * 3, 'Раз в 3 минуты'), (60 * 5, 'Раз в 5 минут',)
    date_time_attempt = models.DateTimeField(default=datetime.now(), verbose_name='Дата и время первой рассылки',
                                             help_text='Введите дату и время первой рассылки. По умолчанию - текущее время')
    date_time_threshold = models.DateTimeField(default=datetime.now(), verbose_name='Дата и время окончания периода',
                                               help_text='Введите дату и время окончания рассылок. По умолчанию - текущее время')
    period = models.IntegerField(default=period_choices[2], choices=period_choices,
                                 help_text='Укажите периодичность рассылки',
                                 verbose_name='Период рассылки')
    status = models.CharField(max_length=100, default='В ожидании', verbose_name='Статус рассылки')
    message = models.ForeignKey(Communication, on_delete=models.CASCADE, verbose_name='Сообщение рассылки')
    client = models.ManyToManyField(Client, related_name='mailings', verbose_name='Клиент рассылки')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец записи', **NULLABLE)

    def __str__(self):
        return (f'Дата попытки последней рассылки{self.date_time_attempt}, дата и время окончания рассылки '
                f'{self.date_time_threshold}')

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('pk',)


class Log(models.Model):
    date_time_last_attempt = models.DateTimeField(default=datetime.now(timezone(TIME_ZONE)),
                                                  verbose_name='Дата и время последней попытки')
    status = models.CharField(default="Не отправлялось", max_length=50, verbose_name='Статус рассылки')
    server_code_response = models.IntegerField(verbose_name='Номер рассылки', **NULLABLE, )
    server_response = models.CharField(max_length=3000, verbose_name='Ответ от сервера', **NULLABLE, )
    mailing_relation = models.ForeignKey(Mailing, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f"{self.date_time_last_attempt} {str(self.server_code_response)}"

    class Meta:
        verbose_name = 'статус рассылки'
        verbose_name_plural = 'статусы рассылок'
        ordering = ('pk',)
