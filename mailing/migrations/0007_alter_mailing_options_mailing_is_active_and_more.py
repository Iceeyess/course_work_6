# Generated by Django 5.0.6 on 2024-08-02 18:10

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_client_owner'),
        ('communications', '0002_communication_owner'),
        ('mailing', '0006_alter_log_options_mailing_owner_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailing',
            options={'ordering': ('pk',), 'permissions': [('view_any_mailing', 'Может просматривать любые рассылки'), ('disable_mailing', 'Может отключать рассылки')], 'verbose_name': 'рассылка', 'verbose_name_plural': 'рассылки'},
        ),
        migrations.AddField(
            model_name='mailing',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Статус рассылки'),
        ),
        migrations.AlterField(
            model_name='log',
            name='date_time_last_attempt',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 2, 18, 10, 30, 365289, tzinfo=datetime.timezone.utc), verbose_name='Дата и время последней попытки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='client',
            field=models.ManyToManyField(related_name='mailings', to='clients.client', verbose_name='Клиент рассылки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='date_time_attempt',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 2, 21, 10, 30, 351621), help_text='Введите дату и время первой рассылки. По умолчанию - текущее время', verbose_name='Дата и время первой рассылки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='date_time_threshold',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 2, 21, 10, 30, 351653), help_text='Введите дату и время окончания рассылок. По умолчанию - текущее время', verbose_name='Дата и время окончания периода'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communications.communication', verbose_name='Сообщение рассылки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='status',
            field=models.CharField(default='В ожидании', max_length=100, verbose_name='Статус рассылки'),
        ),
    ]
