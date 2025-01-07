from rest_framework import serializers
from posts.models import Comment,Post
from users.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']
        read_only_fields = ['id', 'created_at','author']


class PostSerializer(serializers.ModelSerializer):
    
    likes = UserSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Post
        fields = ["id","title","content","created_at","is_public","likes","comments"]
        read_only_fields = ["created_at","likes","id","comments"]