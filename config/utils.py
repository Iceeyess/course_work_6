from datetime import datetime, timedelta
from mailing.models import Mailing, Log
from django.core.mail import send_mass_mail
from config.settings import EMAIL_HOST_USER
from pytz import timezone
from config.settings import TIME_ZONE
from smtplib import (SMTPServerDisconnected, SMTPResponseException, SMTPSenderRefused,
                     SMTPRecipientsRefused, SMTPDataError, SMTPConnectError, SMTPHeloError, SMTPNotSupportedError,
                     SMTPAuthenticationError)


def get_send_mailing() -> None:
    """Функция отправки рассылки."""
    time_zone = timezone(TIME_ZONE)  # Временная зона Django server
    mailing_list = Mailing.objects.all()  # все рассылки
    for mailing in mailing_list:
        period = int(mailing.period.period)  # Период в минутах
        date_time_attempt = mailing.date_time_attempt
        date_time_threshold = mailing.date_time_threshold
        now = datetime.now(time_zone)
        if (date_time_attempt <= now) and (now < date_time_threshold):
            client_email_list = list()
            for client in mailing.client.all():
                client_email_list += [client.email]     # Список email адресов клиентов
            log_instance = Log.objects.create()     # Создает экземпляр класса Log
            log_instance.mailing_relation = mailing
            try:
                args = (mailing.message.topic,
                    mailing.message.body,
                    EMAIL_HOST_USER,
                    client_email_list)
                send_mass_mail(
                    (args,),
                    fail_silently=False,
                )
            except SMTPServerDisconnected as e1:
                response = e1.__doc__
                log_instance.server_code_response = 500
                log_instance.server_response = response
                log_instance.status = 'Ожидает повторную отправку'
            except SMTPResponseException as e2:
                response = e2.__doc__
                log_instance.server_code_response = 500
                log_instance.server_response = response
                log_instance.status = 'Ожидает повторную отправку'

            except SMTPSenderRefused as e3:
                response = e3.__doc__
                log_instance.server_code_response = 400
                log_instance.server_response = response
                log_instance.status = 'Ожидает повторную отправку'
            except SMTPRecipientsRefused as e4:
                response = e4.__doc__
                log_instance.server_code_response = 500
                log_instance.server_response = response
                log_instance.status = 'Ожидает повторную отправку'
            except SMTPDataError as e5:
                response = e5.__doc__
                log_instance.server_code_response = 500
                log_instance.server_response = response
                log_instance.status = 'Ожидает повторную отправку'
            except SMTPConnectError as e6:
                response = e6.__doc__
                log_instance.server_code_response = 500
                log_instance.server_response = response
                log_instance.status = 'Ожидает повторную отправку'
            except SMTPHeloError as e7:
                response = e7.__doc__
                log_instance.server_code_response = 500
                log_instance.server_response = response
                log_instance.status = 'Ожидает повторную отправку'
            except SMTPNotSupportedError as e8:
                response = e8.__doc__
                log_instance.server_code_response = 500
                log_instance.server_response = response
                log_instance.status = 'Ожидает повторную отправку'
            except SMTPAuthenticationError as e9:
                response = e9.__doc__
                log_instance.server_code_response = 400
                log_instance.server_response = response
                log_instance.status = 'Ожидает повторную отправку'
            else:
                log_instance.server_code_response = 200
                log_instance.status = 'Сообщение отправлено'
                mailing.status = 'Сообщение отправлено'
                log_instance.server_response = 'No errors'

            finally:
                mailing.date_time_attempt = now + timedelta(minutes=period)
                log_instance.date_time_last_attempt = now
                log_instance.save()
                mailing.save()

        elif (date_time_attempt <= now) and (now > date_time_threshold):
            mailing.status = 'Процесс рассылок завершен'
            mailing.date_time_attempt = now
            mailing.save()
        else:
            continue
