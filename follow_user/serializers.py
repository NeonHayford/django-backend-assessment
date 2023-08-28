from rest_framework import serializers
from .models import Follower

class FollowerSerializer(serializers.Serializer):

    class Meta:
        models = Follower
        fields = '__all__'
