from django.core.management import BaseCommand
from config.services import get_send_mailing


class Command(BaseCommand):

    def handle(self, *args, **options):
        get_send_mailing()