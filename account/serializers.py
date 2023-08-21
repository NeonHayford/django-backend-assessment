from .models import UserProfile
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers


class RegisterSerializer(UserCreateSerializer):
    full_name = serializers.CharField(read_only=True)
    class Meta(UserCreateSerializer.Meta):
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'full_name']



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        models = UserProfile
        fields = '__all__'