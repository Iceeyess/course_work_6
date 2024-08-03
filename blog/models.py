import datetime

from django.db import models
from datetime import datetime
import random
# Create your models here.

NULLABLE = dict(null=True, blank=True)


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок", help_text="Введите заголовок")
    body_blog = models.TextField(verbose_name="Содержимое статьи", help_text="Введите текст статьи")
    picture = models.ImageField(upload_to='blog/', verbose_name="Фото", help_text="Загрузите фото", **NULLABLE)
    count_view = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")
    posted_date = models.DateTimeField(default=datetime.now(), auto_created=True, verbose_name="Дата создания статьи")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('pk', )



