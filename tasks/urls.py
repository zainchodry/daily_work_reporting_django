from django.urls import path

from .views import *

urlpatterns = [

    path(
        "",
        TaskListCreateView.as_view()
    ),

    path(
        "my-tasks/",
        MyTaskListView.as_view()
    ),

    path(
        "<int:pk>/update-status/",
        UpdateTaskStatusView.as_view()
    ),

]