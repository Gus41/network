from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True) 

    class Meta:
        model = User
        fields = ['id', 'username', 'email']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already in use")
        return value
    
    def create(self, validated_data):
        
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        
        return user