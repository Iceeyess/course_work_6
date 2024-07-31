import os
from datetime import datetime, timedelta
from mailing.models import Mailing, Log
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from pytz import timezone
from config.settings import TIME_ZONE
from smtplib import (SMTPServerDisconnected, SMTPResponseException, SMTPSenderRefused,
                     SMTPRecipientsRefused, SMTPDataError, SMTPConnectError, SMTPHeloError, SMTPNotSupportedError,
                     SMTPAuthenticationError)


def get_send_mailing() -> None:
    """Функция отправки рассылки."""
    time_zone = timezone(TIME_ZONE)  # Временная зона Django server
    mailing_list = Mailing.objects.filter(is_active=True)  # все рассылки
    for mailing in mailing_list:
        period = mailing.period  # Период в минутах
        date_time_attempt = mailing.date_time_attempt
        date_time_threshold = mailing.date_time_threshold
        now = datetime.now(time_zone)
        status_uncompleted_task = ['В ожидании', 'Ожидает повторную отправку', 'Сообщение отправлено', ]
        if mailing.status in status_uncompleted_task:
            if (date_time_attempt <= now) and (now < date_time_threshold):
                client_email_list = [client.email for client in mailing.client.all()]  # Список email адресов клиентов
                log_instance = Log.objects.create()     # Создает экземпляр класса Log
                log_instance.mailing_relation = mailing  # Связывает экземпляр класса Log с экземпляром класса Mailing
                # Блок отправки сообщения
                try:
                    send_mail(mailing.message.topic, mailing.message.body, EMAIL_HOST_USER, client_email_list,
                              fail_silently=False)

                except (SMTPServerDisconnected, SMTPResponseException, SMTPRecipientsRefused, SMTPDataError,
                        SMTPConnectError, SMTPHeloError, SMTPNotSupportedError):
                    response = 'Ошибка со стороны сервера'
                    log_instance.server_code_response = 500
                    log_instance.server_response = response
                    log_instance.status = 'Ожидает повторную отправку'
                    mailing.status = 'Ожидает повторную отправку'

                except (SMTPSenderRefused, SMTPAuthenticationError):
                    response = 'Ошибка отправки сообщения'
                    log_instance.server_code_response = 400
                    log_instance.server_response = response
                    log_instance.status = 'Ожидает повторную отправку'
                    mailing.status = 'Ожидает повторную отправку'

                else:
                    response = 'Отправлено без ошибок'
                    log_instance.server_code_response = 200
                    log_instance.status = 'Сообщение отправлено'
                    mailing.status = 'Сообщение отправлено'
                    log_instance.server_response = response

                finally:
                    mailing.date_time_attempt = now + timedelta(seconds=period)
                    log_instance.date_time_last_attempt = now
                    log_instance.save()
                    mailing.save()

            # блок закрытия процесса рассылки:
            elif now > date_time_threshold:
                mailing.status = 'Процесс рассылок завершен'
                mailing.date_time_attempt = now
                mailing.save()


def send_registration_email(form, link) -> None:
    subject = 'Registration is done in Sky mailing.'
    body = f'''Congratulations, {form['first_name']}.
    You have been registered at the Sky mailing resource.
    Here are output credentials:
    Your email: {form['email']}.
    Your password: {form['password1']}.
    Your first name: {form['first_name']}
    Your last name: {form['last_name']}.
    Please follow the link to complete registration and approve.
    {link}
    regards,
    Administration'''

    email_sender = os.getenv('EMAIL_HOST_USER')
    email_receiver = form['email']
    send_mail(subject=subject, message=body, from_email=email_sender, recipient_list=[email_receiver])
