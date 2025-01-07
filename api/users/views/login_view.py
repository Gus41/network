from rest_framework.views import APIView
from django.http import HttpRequest
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class LoginView(APIView):
    http_method_names = ["post"]  

    def post(self, request: HttpRequest, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"detail": "Both 'username' and 'password' are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = get_object_or_404(User, username=username)

        if not user.check_password(password):
            return Response(
                {"detail": "Invalid credentials."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                "message": "Login successful.",
                "token": token.key,
                "user": {"username": user.username, "email": user.email, "id": user.id},
            },
            status=status.HTTP_200_OK,
        )
