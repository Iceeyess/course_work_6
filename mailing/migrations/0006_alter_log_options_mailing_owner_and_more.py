# Generated by Django 5.0.6 on 2024-07-30 19:22

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0005_alter_log_date_time_last_attempt_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='log',
            options={'ordering': ('pk',), 'verbose_name': 'статус рассылки', 'verbose_name_plural': 'статусы рассылок'},
        ),
        migrations.AddField(
            model_name='mailing',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
        migrations.AlterField(
            model_name='log',
            name='date_time_last_attempt',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 30, 19, 22, 15, 658544, tzinfo=datetime.timezone.utc), verbose_name='Дата и время последней попытки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='date_time_attempt',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 30, 22, 22, 15, 645167), help_text='Введите дату и время первой рассылки. По умолчанию - текущее время', verbose_name='Дата и время первой рассылки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='date_time_threshold',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 30, 22, 22, 15, 645196), help_text='Введите дату и время окончания рассылок. По умолчанию - текущее время', verbose_name='Дата и время окончания периода'),
        ),
    ]
