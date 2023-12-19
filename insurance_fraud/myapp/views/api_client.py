from django.core.mail import send_mail
from django.conf import settings


def sendmail(request):
    subject = 'testing email using gmail'
    message = 'testing 123.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['araf66174@gmail.com']

    send_mail(subject, message, from_email, recipient_list)