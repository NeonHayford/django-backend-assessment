from django.urls import path, include
from .views import FollowersView

urlpatterns = [
    # path('auth/logout', LogoutView.as_view(), name='logout'),
    path('', include('user_channels.urls')),
    path('', include('user_groups.urls')),
    path('follow/user/',FollowersView.as_view(), name='user_following')
]