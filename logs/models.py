from django.db import models
from datetime import datetime
from pytz import timezone
from config.settings import TIME_ZONE
from mailing.models import Mailing

# Create your models here.

NULLABLE = dict(null=True, blank=True)


class Log(models.Model):
    """Модель для логирования рассылок"""
    date_time_last_attempt = models.DateTimeField(default=datetime.now(timezone(TIME_ZONE)),
                                                  verbose_name='Дата и время последней попытки')
    status = models.CharField(default="Не отправлялось", max_length=50, verbose_name='Статус рассылки')
    server_code_response = models.IntegerField(verbose_name='Номер рассылки', **NULLABLE, )
    server_response = models.CharField(max_length=3000, verbose_name='Ответ от сервера', **NULLABLE, )
    mailing_relation = models.ForeignKey(Mailing, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f"{self.date_time_last_attempt} {str(self.server_code_response)}"

    class Meta:
        verbose_name = 'статус рассылки'
        verbose_name_plural = 'статусы рассылок'
        ordering = ('pk',)
