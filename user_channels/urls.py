from django.urls import path
from .views import *

urlpatterns = [
    #channels
    path('create/channel', CreateChannelView.as_view(), name='create_channel'),
    path('<str:author>/channel/<str:pk>', UpateChannelView.as_view(), name='upate_channel'),
    path('remove/<str:author>/channel/<str:pk>', DeleteChannelView.as_view(), name='delete_channel'),

    # Channel Profile Image
    path('channel/image', CreateChannelProfileView.as_view(), name='create_channel_profile'),
    path('image/<str:image_id>/channel/<str:channel_id>', UpateChannelProfileView.as_view(), name='upate_channel_profile'),
    path('remove/image/<str:image_id>/channel/<str:channel_id>', DeleteChannelProfileView.as_view(), name='delete_channel_profile'),
    
    # Channel Post
    path('channel/post', CreateChannelPostView.as_view(), name='create_channel_post'),
    path('channel/post/<str:post_id>', DeleteChannelPostView.as_view(), name='delete_channel_post'),

    #Post likes from users
    path('channel/likes/post', AddChannelPostLikeView.as_view(), name='like_channel_post'),
    path('channel/<str:likes>/likes/post', RemoveChannelPostLikeView.as_view(), name='delete_channel_post')
]