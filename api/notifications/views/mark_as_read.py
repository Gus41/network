from rest_framework.views import APIView
from rest_framework.response import Response
from notifications.models import Notification

class MarkAsReadView(APIView):
    http_method_names = ['post']
    
    def post(self, request, pk):
        try:
            notification = Notification.objects.get(id=pk, recipient=request.user)
            notification.is_read = True
            notification.save()
            return Response({"message": "Notification marked as read."}, status=200)
        except Notification.DoesNotExist:
            return Response({"error": "Notification not found."}, status=404)
