from rest_framework.viewsets import ModelViewSet
from relationships.models import Follow
from relationships.serializers import FollowSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework import status

class FollowView(ModelViewSet):
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()
    permission_classes = [ IsAuthenticated ]
    
    http_method_names = ["post","delete"]
    
    def create(self, request: HttpRequest, *args, **kwargs):
        

        if int(request.data["follower"]) != request.user.id:  
            return Response({"detail": "You don't have permission to do this"}, status=status.HTTP_400_BAD_REQUEST)

        
        if request.data['follower'] == request.data['followed']:
            return Response(
                "You cant follow yourself",
                status=status.HTTP_400_BAD_REQUEST
            )
            
        if Follow.objects.filter(follower=request.user,followed=request.data['followed']).exists():
            return Response(
                "You are alredy following this user",
                status=status.HTTP_400_BAD_REQUEST
            )
    
        return super().create(request, *args, **kwargs)

    
    def destroy(self, request: HttpRequest, *args, **kwargs):
        follow = self.get_object()
        
        if request.user != follow.follower:
            return Response(
                "No permission",
                status=status.HTTP_400_BAD_REQUEST
            )
        
        return super().destroy(request, *args, **kwargs)