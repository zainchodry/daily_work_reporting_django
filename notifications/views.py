from rest_framework.generics import (
    ListAPIView,
    UpdateAPIView
)

from rest_framework.permissions import (
    IsAuthenticated
)

from .models import Notification

from .serializers import (
    NotificationSerializer
)


class MyNotificationView(
    ListAPIView
):

    serializer_class = (
        NotificationSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]


    def get_queryset(
        self
    ):

        return Notification.objects.filter(
            receiver=self.request.user
        ).order_by(
            "-created_at"
        )
    
class MarkNotificationReadView(
    UpdateAPIView
):

    serializer_class = (
        NotificationSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]


    def get_queryset(
        self
    ):

        return Notification.objects.filter(
            receiver=self.request.user
        )