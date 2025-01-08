from django.contrib import admin
from relationships.models import Follow
# Register your models here.
@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("follower","followed")
    