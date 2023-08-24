from django.urls import path
from .views import *

urlpatterns = [
    #channels
    path('create/channel/', CreateChannelView.as_view(), name='create_channel'),
    path('', UpateChannelView.as_view(), name='upate_channel'),
    path('', DeleteChannelView.as_view(), name='delete_channel'),
    # Channel Profile Image
    # path('', CreateChannelProfileView.as_view(), name='create_channel_profile'),
    # path('', UpateChannelProfileView.as_view(), name='upate_channel_profile'),
    # path('', DeleteChannelProfileView.as_view(), name='delete_channel_profile'),
    # Channel Post
    # path('', CreateChannelPostView.as_view(), name='create_channel_post'),
    # path('', DeleteChannelPostView.as_view(), name='delete_channel_post'),
    #Post likes from users
    # path('', AddChnnelPostLikeView.as_view(), name='like_channel_post'),
    # path('', RemoveChannelPostLikeView.as_view(), name='delete_channel_post')
]