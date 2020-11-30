from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from virtuagym import settings


def get_random_user():
    return get_user_model().objects.first()


def email_to(receiver, plan_name):
    subject = 'New plan!'
    message = f'You just got a new plan! {plan_name}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['gerardotatzati@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
