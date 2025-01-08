from django.urls import path
from rest_framework.routers import SimpleRouter
from relationships.views import FollowView

router = SimpleRouter()

router.register(r'follow',FollowView,basename='follow')

urlpatterns = [
    
]
urlpatterns += router.urls