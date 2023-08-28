from rest_framework import serializers
from .models import *


class GroupSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    chat_profile = serializers.ImageField(required=False)
    class Meta:
        model = Group
        fields = ('id', 'group_name', 'member', 'author', 'created_at',)

class MessagelikesSerializer(serializers.Serializer):
    class Meta:
        model = MessageLikes
        fields = '__all__'
        
class MessageSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    image = serializers.ImageField(required=False)
    video = serializers.FileField(required=False)
    likes = serializers.SerializerMethodField()
    class Meta:
        model = ChatMessage
        fields = '__all__'

    def get_likes(self, post):
        message_like = MessageLikes.objects.filter(post=post).count()
        return message_like
    
class CommentlikesSerializer(serializers.Serializer):
    class Meta:
        model = CommentLikes
        fields = '__all__'

class CommentSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    image = serializers.ImageField(required=False)
    video = serializers.FileField(required=False)
    likes = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = '__all__'

    def get_likes(self, post):
        comment_like = CommentLikes.objects.filter(post=post).count()
        return comment_like
    
class ReplylikesSerializer(serializers.Serializer):
    class Meta:
        model = ReplyLikes
        fields = '__all__'

class ReplySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    image = serializers.ImageField(required=False)
    video = serializers.FileField(required=False)
    likes = serializers.SerializerMethodField()
    class Meta:
        model = Reply
        fields = '__all__'

    def get_likes(self, post):
        reply_like = ReplyLikes.objects.filter(post=post).count()
        return reply_like