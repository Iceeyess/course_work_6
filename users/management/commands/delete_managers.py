from django.contrib.auth.models import Permission, Group
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Функция удаления группы managers для тестирования"""

    def handle(self, *args, **options):
        group = Group.objects.all()
        group.delete()
