from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Follow

class FollowSerializer(serializers.ModelSerializer):

    follower = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    followed = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ['id','follower', 'followed']
