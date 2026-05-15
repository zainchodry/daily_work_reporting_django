from django.db import models
from accounts.models import User


class Notification(models.Model):

    TYPE_CHOICES = (
        ("TASK_ASSIGNED", "Task Assigned"),
        ("REPORT_SUBMITTED", "Report Submitted"),
        ("REPORT_APPROVED", "Report Approved"),
        ("REPORT_REJECTED", "Report Rejected"),
    )

    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    title = models.CharField(
        max_length=255
    )

    message = models.TextField()

    notification_type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES
    )

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.title