from django.core.mail import send_mail

from .models import Notification


def create_notification(
    receiver,
    title,
    message,
    notification_type
):

    Notification.objects.create(
        receiver=receiver,
        title=title,
        message=message,
        notification_type=notification_type
    )


def send_email_notification(
    user,
    subject,
    message
):

    send_mail(
        subject=subject,
        message=message,
        from_email=None,
        recipient_list=[user.email]
    )