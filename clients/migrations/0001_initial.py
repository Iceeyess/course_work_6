# Generated by Django 5.0.6 on 2024-07-28 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Введите электронную почту', max_length=254, verbose_name='Электронная почта')),
                ('full_name', models.CharField(help_text='Введите Ф.И.О.', max_length=100, verbose_name='Ф.И.О.')),
                ('comment', models.TextField(help_text='Введите комментарий', verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ('pk',),
            },
        ),
    ]
