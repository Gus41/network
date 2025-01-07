from django.urls import path
from users.views import RegisterView, LoginView, MeView,UserProfileView

urlpatterns = [
    path('signup/',RegisterView.as_view(),name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('me/',MeView.as_view(),name='me'),
    path('<str:username>/',UserProfileView.as_view(),name="profile"),
]