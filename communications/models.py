from django.db import models

# Create your models here.


class Communication(models.Model):
    topic = models.CharField(max_length=100, verbose_name='Тема коммуникации', help_text='Введите тему сообщения')
    body = models.TextField(verbose_name='Текст сообщения', help_text='Введите текст сообщения')

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ('pk', )