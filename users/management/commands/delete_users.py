from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Функция удаления всех пользователей"""

    def handle(self, *args, **options):
        user = User.objects.all()
        user.delete()
