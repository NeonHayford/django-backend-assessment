from django.urls import path
from .views import *

urlpatterns = [
    # path('auth/logout', LogoutView.as_view(), name='logout'),
    # Group
    path('create/group', CreateGroupView.as_view(), name='create_group'),
    path('<str:author_id>/channel/<str:pk>', UpateGroupView.as_view(), name='upate_group'),
    path('remove/<str:author_id>/channel/<str:pk>', DeleteGroupView.as_view(), name='delete_group'),

    # Group Message
    path('group/message', CreateChatMessageView.as_view(), name='create_group_message'),
    path('group/<str:pk>/message/<str:author_id>', DeleteChatMessageView.as_view(), name='delete_group_message'),

    # Message likes from users
    path('group/message/likes', CreateMessageLikesView.as_view(), name='like_group_message'),
    path('group/<str:likes>/message/likes', DeleteMessageLikesView.as_view(), name='delete_group_message'),

    # Group Comments
    path('group/comment', CreateCommentView.as_view(), name='create_group_comment'),
    path('group/<str:comment_id>/comment/<str:author_id>', DeleteCommentView.as_view(), name='delete_group_comment'),

    # Comment likes from users
    path('group/comment/likes', CreateCommentLikesView.as_view(), name='like_group_comment'),
    path('group/<str:likes>/comment/likes', DeleteCommentLikesView.as_view(), name='delete_group_comment'),

    # Group Reply
    path('group/comment', CreateReplyView.as_view(), name='create_group_comment'),
    path('group/<str:pk>/comment/<str:author_id>', DeleteReplyView.as_view(), name='delete_group_comment'),

    # Reply likes from users
    path('group/reply/likes', CreateReplyLikesView.as_view(), name='like_group_reply'),
    path('group/<str:likes>/reply/likes', DeleteReplyLikesView.as_view(), name='delete_group_reply'),
]
