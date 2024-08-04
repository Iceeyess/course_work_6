from django.core.management import BaseCommand
from config.services import get_send_mailing


class Command(BaseCommand):
    """Одиночная команда проверки и отправки сообщений,
    чтобы не включать crontab"""

    def handle(self, *args, **options):
        get_send_mailing()