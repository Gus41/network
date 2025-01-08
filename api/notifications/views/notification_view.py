from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from notifications.models import Notification

class NotificationListView(APIView):
    http_method_names = ['get']
    
    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user, is_read=False)
        serialized = [
            {"id": n.id, "type": n.type, "message": n.message, "created_at": n.created_at}
            for n in notifications
        ]
        return Response(serialized, status=status.HTTP_200_OK)
