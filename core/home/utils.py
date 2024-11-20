from django.core.mail import send_mail, EmailMessage
from django.conf import settings

def send_email_to_client():
    subject = ''
    message = ''
    from_email = settings.EMAIL_HOST_USER
    receipient_list = ['tejas@gmail.com']
    send_mail(subject, message, from_email, receipient_list)


def send_email_with_attachment(subject, message, receipient_list, file_path):
    mail = EmailMessage(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER
                        to = receipient_list)

    mail.attach_file(file_path)
    mail.send()