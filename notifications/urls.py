from django.urls import path

from .views import *

urlpatterns = [

    path(
        "",
        MyNotificationView.as_view()
    ),

    path(
        "<int:pk>/read/",
        MarkNotificationReadView.as_view()
    ),

]