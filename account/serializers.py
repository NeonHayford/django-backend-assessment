from .models import *
from djoser.serializers import UserCreateSerializer


class RegisterSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        
        fields = ['id', 'first_name', 'last_name', 'email', 'password']