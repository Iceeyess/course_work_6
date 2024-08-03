from django.core.exceptions import ObjectDoesNotExist
from django.core.management import BaseCommand

from users.models import User
from django.contrib.auth.models import Permission, Group


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        Функция создания группы managers, а так же наделением полномочий по условию ТЗ.
        Если группа managers не создана, то создаем ее. Группе managers назначаем сотрудника.
        """
        perms_list = ('view_any_mailing', 'disable_mailing', 'view_any_user', 'disable_user' )
        new_group, is_created_group = Group.objects.get_or_create(name='managers')
        for perms in perms_list:
            try:
                new_group.permissions.get(codename=perms)
            except ObjectDoesNotExist:
                print('Назначаю полномочия...')
                new_group.permissions.add(Permission.objects.get(codename=perms))
                print(f'Полномочия {perms} были добавлены...')
            finally:
                user = User.objects.get(is_staff=True, email='iceeyesss@yandex.ru')
                new_group.user_set.add(user)


