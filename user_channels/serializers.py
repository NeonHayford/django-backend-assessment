from rest_framework import serializers
from .models import Channel,  ChannelProfile, ChannelPost, ChannelPostLikes


class ChannelSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only = True)

    class Meta:
        model = Channel
        fields = '__all__'

        

class ChannelProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelProfile
        fields = '__all__'


class PostLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelPostLikes
        fields = '__all__'


class ChannelPostSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only = True)
    channel_image = serializers.ImageField(required=False)
    channel_video = serializers.FileField(required=False)
    likes = serializers.SerializerMethodField()

    class Meta:
        model = ChannelPost
        fields = '__all__'
        # depth = 5


    def get_likes(self, post_id):
        query = ChannelPostLikes.objects.filter(post_id=post_id).exists()
        return query
