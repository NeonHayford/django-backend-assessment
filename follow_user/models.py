from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    following = models.ManyToManyField(User, through=user, symmetrical=False, related_name='follow_user')
    
