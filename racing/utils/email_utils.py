from django.core.mail import send_mail

from vietnamracing import settings


def send_email(subject, message, to_email):
    from_email = settings.EMAIL_HOST_USER
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, [to_email])
        except Exception as e:
            print(str(e))
