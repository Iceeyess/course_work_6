from datetime import datetime, timedelta
from mailing.models import Mailing
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from pytz import timezone
from config.settings import TIME_ZONE


def get_send_mailing():
    time_zone = timezone(TIME_ZONE)
    mailing_list = Mailing.objects.all()
    for mailing in mailing_list:
        period = int(mailing.period.period)
        date_time_first_try = mailing.date_time_first_try
        date_time_threshold = mailing.date_time_threshold
        now = datetime.now(time_zone)
        if date_time_first_try <= now and now < date_time_threshold:
            for client in mailing.client.all():
                send_mail(
                    mailing.message.topic,
                    mailing.message.body,
                    EMAIL_HOST_USER,
                    [client.email],
                    fail_silently=False,
                )
            n = Status.objects.create()
            mailing.status.log.status
            mailing.date_time_first_try += timedelta(minutes=period)
            mailing.save()
        else:
            continue
