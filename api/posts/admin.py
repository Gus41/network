from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_public', 'like_count') 
    list_filter = ('is_public', 'created_at') 
    search_fields = ('title', 'content', 'author__username')
    ordering = ('-created_at',) 
    list_editable = ('is_public',)  
    date_hierarchy = 'created_at'  
    
    def like_count(self, obj):
        return obj.likes.count()  
    like_count.short_description = 'Likes'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at', 'content_snippet') 
    list_filter = ('created_at',)  
    search_fields = ('content', 'author__username', 'post__title')  
    ordering = ('-created_at',)  
    date_hierarchy = 'created_at'  
    
    def content_snippet(self, obj):
        return obj.content[:50]  
    content_snippet.short_description = 'Content'
