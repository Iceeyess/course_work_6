from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Функция создания 3х пользователей с разными вариациями полномочий для тестирования"""

    def handle(self, *args, **options):
        super_user = User.objects.create(
            username='Admin',
            email='ice_eyes@mail.ru',
            is_superuser=True,
            is_staff=True,
            is_active=True,
            first_name='Дмитрий',
            last_name='Крашенинников',
        )
        super_user.set_password('123456')
        super_user.save()
        user = User.objects.create(
            username='Антоша',
            email='iceeyesss@yandex.ru',
            is_superuser=False,
            is_staff=True,
            is_active=True,
            first_name='Антоша',
            last_name='Гагарин',
        )
        user.set_password('123456')
        user.save()
        low_user = User.objects.create(
            username='Павлик',
            email='pavlikkrolikov@yandex.ru',
            is_superuser=False,
            is_staff=False,
            is_active=True,
            first_name='Павлик',
            last_name='Кроликов',
        )
        low_user.set_password('123456')
        low_user.save()