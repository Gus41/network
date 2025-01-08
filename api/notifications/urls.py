from django.urls import path

from notifications.views import NotificationListView
from notifications.views import MarkAsReadView

urlpatterns = [
    path("",NotificationListView.as_view(),name="notification"),
    path("read/<int:pk>",MarkAsReadView.as_view(),name="read")      
]