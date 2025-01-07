from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpRequest
from django.contrib.auth.models import User

class MeView(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get','patch']

    def get(self, request, *args, **kwargs):
        user = request.user 

        return Response(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            },
            status=status.HTTP_200_OK,
        )
        
    def patch(self, request: HttpRequest, *args, **kwargs):
        user = request.user
        
        # Atualizar campos específicos
        first_name = request.data.get('first_name', None)
        last_name = request.data.get('last_name', None),
        username = request.data.get('username', None)
        
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if username:
            if User.objects.filter(username=username).exists():
                return Response(
                    {"detail": "Username already in use"},
                    status=status.HTTP_400_BAD_REQUEST  # Usar o código 400, pois é um erro de entrada de dados
                )
            user.username = username

        
        # Salve as alterações
        user.save()
        
        return Response(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            },
            status=status.HTTP_200_OK,
        )