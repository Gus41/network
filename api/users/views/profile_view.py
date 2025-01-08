from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from relationships.models import Follow

class UserProfileView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, username, *args, **kwargs):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        followers = Follow.objects.filter(followed=user)[:10]
        followers_list = [
            {"id": follower.follower.id, "username": follower.follower.username}
            for follower in followers
        ]
        
        _following = Follow.objects.filter(follower=user)[:10]
        
        following_list = [
            {"id": following.followed.id, "username": following.followed.username}
            for following in _following
        ]
        return Response(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "followers": followers_list,  
                "following": following_list
            },
            status=status.HTTP_200_OK
        )
