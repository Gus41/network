from rest_framework.routers import DefaultRouter
from .views import PostView
from django.urls import path

router = DefaultRouter()
router.register(r'', PostView, basename='post')

urlpatterns = [
    path("<int:pk>/like/", PostView.as_view({"post":"like"}),name='like'),
    path("<int:pk>/comment/", PostView.as_view({"post":"comment"}),name='comment')
]

urlpatterns += router.urls
