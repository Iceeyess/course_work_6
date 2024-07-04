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
        period = datetime.strftime(mailing.period, '%Y-%m-%d %H:%M:%S+%f')
        if (datetime.strptime(mailing.date_time_first_try, '%Y-%m-%d %H:%M:%S+%f') < datetime.now()
                and datetime.now() < datetime.strptime(mailing.date_time_threshold, '%Y-%m-%d %H:%M:%S+%f')):
            mailing.status.all.log.status = 'Отправлено'
            mailing.date_time_first_try = datetime.now()
            mailing.save()
            for client in mailing.client.all():
                send_mail(
                    mailing.message.topic,
                    mailing.message.body,
                    EMAIL_HOST_USER,
                    [mailing.client],
                    fail_silently=False,
                )
            mailing.date_time_first_try
        else:
            continue
