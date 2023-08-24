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
    like_post = serializers.SerializerMethodField()

    class Meta:
        model = ChannelPost
        fields = '__all__'


    def get_like_post(self, post):
        user = self.context['request'].user
        query = ChannelPostLikes.objects.filter(post=post, liker=user).exists()
        return query

# image
# allow_emptyfile = False
# allow_null = False
# use_url = True
# required = False
# max_length = None