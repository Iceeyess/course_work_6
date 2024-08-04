from django.db import models

from users.models import User


# Create your models here.
NULLABLE = dict(blank=True, null=True)


class Communication(models.Model):
    """Модель сообщений"""
    topic = models.CharField(max_length=100, verbose_name='Тема коммуникации', help_text='Введите тему сообщения')
    body = models.TextField(verbose_name='Текст сообщения', help_text='Введите текст сообщения')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец записи', **NULLABLE)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ('pk', )