from rest_framework.generics import CreateAPIView
from django.http import HttpRequest
from users.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

class RegisterView(CreateAPIView):
    serializer_class = UserSerializer
    
    def create(self, request: HttpRequest, *args, **kwargs):
        
        serializer = self.get_serializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        
        self.perform_create(serializer)
        
        user = serializer.instance
        
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=user)
        
        
        return Response(
            {'token': token.key,
             'Message': 'User created'},
            status=status.HTTP_201_CREATED,
            headers=headers
        )
        
        
        
    
    