from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    
    likes = models.ManyToManyField(
        User,
        related_name="likes",
        blank=True
    )
    
    is_public = models.BooleanField(default=True) 
    
    def __str__(self):
        return self.title or f"Post by {self.author.username}"

    class Meta:
        ordering = ["-created_at"] 
        
        
        
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.CASCADE
    )
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação do comentário

    def __str__(self):
        return f"{self.author.username}: {self.content[:10]}..."