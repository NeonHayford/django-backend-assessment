from rest_framework import serializers
from .models import UserChannel, ChannelPost


class UserChannelSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required = False, use_url = True, max_length = None, allow_null = False, allow_empty = False)

    class Meta:
        models = UserChannel
        fields = '__alll__'


class Request(serializers.ModelSerializer):
    channel_content = serializers.TextField()
    channel_image = serializers.ImageField(required=False)
    channel_video = serializers.FileField(required=False)
    # like_post = serializers.

    class Meta:
        models = ChannelPost
        fields = '__all__'

# image
# allow_emptyfile = False
# allow_null = False
# use_url = True
# required = False
# max_length = None