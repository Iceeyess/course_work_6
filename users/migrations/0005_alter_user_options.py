# Generated by Django 5.0.6 on 2024-08-02 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('pk',), 'permissions': [('view_any_user', 'Может просматривать список пользователей сервиса'), ('disable_user', 'Может блокировать пользователей сервиса')], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
