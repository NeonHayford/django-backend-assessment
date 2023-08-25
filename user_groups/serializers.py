from rest_framework import serializers
from .models import Group, ChatMessage, Comment, Reply


class GroupSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    chat_profile = serializers.ImageField(required=False)
    class Meta:
        model = Group
        fields = ('id', 'group_name', 'member', 'author', 'created_at',)


class ChatMessageSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    image = serializers.ImageField(required=False)
    video = serializers.FileField(required=False)
    like_post = serializers.SerializerMethodField()
    class Meta:
        model = ChatMessage
        fields = '__all__'

    def get_like_post(self, post):
        user = self.member['request'].user
        message_like = ChatMessage.objects.filter(post=post, liker=user).exists()
        return message_like
    

class CommentSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    image = serializers.ImageField(required=False)
    video = serializers.FileField(required=False)
    like_post = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = '__all__'

    def get_like_post(self, post):
        user = self.context['request'].user
        comment_like = Comment.objects.filter(post=post, liker=user).exists()
        return comment_like
    

class ReplySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    image = serializers.ImageField(required=False)
    video = serializers.FileField(required=False)
    like_post = serializers.SerializerMethodField()
    class Meta:
        model = Reply
        fields = '__all__'

    def get_like_post(self, post):
        user = self.context['request'].user
        comment_like = Reply.objects.filter(post=post, liker=user).exists()
        return comment_like