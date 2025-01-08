from rest_framework.viewsets import ModelViewSet
from posts.models import Post,Comment
from posts.serializers import PostSerializer,CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpRequest
from rest_framework.decorators import action
from notifications.models import Notification

class PostView(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_fields = ['author', 'is_public']
    search_fields = ['title', 'content', 'author__username']
    ordering_fields = ['created_at', 'likes']
    
    @action(detail=True,methods=['post'])
    def like(self, request: HttpRequest, pk=None):
        post = self.get_object()
        if request.user in post.likes.all():
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        
        post.likes.add(request.user)
        #create an notification
        Notification.objects.create(
            recipient=post.author,
            type="Like",
            message=f'{request.user} liked your post!',
            
        )
        return Response({"detail": "Post liked successfully."}, status=status.HTTP_200_OK)
    
    
    @action(detail=True,methods=['post'])
    def comment(self, request: HttpRequest, pk=None):
        post = self.get_object()  
        data = request.data
        data['post'] = post.id
        
        
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(post=post, author=request.user)
             #create an notification
            Notification.objects.create(
                recipient=post.author,
                type="Comment",
                message=f'{request.user} commented your post!',
                
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, *args, **kwargs):
        posts = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(posts,many=True)
        
        return Response(
            serializer.data
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
        
    def partial_update(self, request: HttpRequest, *args, **kwargs):
        instance = self.get_object()
        
        if instance.author != request.user:
            return Response(
                "You dont have permission to do this",
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response(
            serializer.data
        )