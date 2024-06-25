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
        ordering = ('pk', )


class Period(models.Model):
    period = models.CharField(default=False, verbose_name='Период', help_text='Введите период')

    class Meta:
        verbose_name = 'период'
        verbose_name_plural = 'периоды'


class Status(models.Model):
    period = models.CharField(default=False, verbose_name='Статус', help_text='Введите статус отправки')

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'статусы'


class Message(models.Model):
    topic = models.CharField(max_length=100, verbose_name='Тема сообщения', help_text='Введите тему сообщения')
    text = models.TextField(verbose_name='Текст сообщения', help_text='Введите текст сообщения')

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Mailing(models.Model):
    date_time_first_try = models.DateTimeField(verbose_name='Тема сообщения', help_text='Введите тему сообщения')
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'