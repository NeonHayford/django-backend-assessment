from rest_framework import serializers
from .models import follower

class FollowerSerializer(serializers.Serializer):

    class Meta:
        models = follower
        fields = '__all__'
