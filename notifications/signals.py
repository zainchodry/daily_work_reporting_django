from django.db.models.signals import post_save
from django.dispatch import receiver

from tasks.models import Task

from .services import (
    create_notification,
    send_email_notification
)


@receiver(
    post_save,
    sender=Task
)
def task_created_notification(
    sender,
    instance,
    created,
    **kwargs
):

    if created:

        title = "New Task Assigned"

        message = (
            f"You have been assigned task: "
            f"{instance.title}"
        )

        create_notification(
            receiver=instance.assigned_to,
            title=title,
            message=message,
            notification_type="TASK_ASSIGNED"
        )

        send_email_notification(
            user=instance.assigned_to,
            subject=title,
            message=message
        )