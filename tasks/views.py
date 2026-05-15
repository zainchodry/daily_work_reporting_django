from rest_framework.generics import (
    ListCreateAPIView, ListAPIView, UpdateAPIView,
)

from rest_framework.permissions import (
    IsAuthenticated
)

from .models import Task
from .serializers import TaskSerializer
from .permissions import (
    IsAdminOrManager
)


class TaskListCreateView(
    ListCreateAPIView
):

    serializer_class = TaskSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminOrManager
    ]

    def get_queryset(self):

        return Task.objects.all()


    def perform_create(
        self,
        serializer
    ):

        serializer.save(
            assigned_by=self.request.user
        )

class MyTaskListView(
    ListAPIView
):

    serializer_class = TaskSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):

        return Task.objects.filter(
            assigned_to=self.request.user
        )
    
class UpdateTaskStatusView(
    UpdateAPIView
):

    serializer_class = TaskSerializer

    permission_classes = [
        IsAuthenticated
    ]

    queryset = Task.objects.all()


    def get_queryset(
        self
    ):

        return Task.objects.filter(
            assigned_to=self.request.user
        )