from django.db import models
from django.contrib.auth.models import User
from  core import settings
from datetime import datetime, date

# Create your models here.
class UserChannel(models.Model):
    pass
    

class UserGroup(models.Model):
    group_name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    chat_profile = models.ImageField(upload_to='chat_profile/%h.jpg')
    member= models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='multiple_users')
    owner = models.ForeignKey(User, on_delete= models.CASCADE,related_name = 'user_group')
    created_date = models.DateTimeField(auto_now_add=datetime.now())


class Chat_message(models.Model):
    community = models.ForeignKey(UserGroup, on_delete=models.CASCADE, related_name='chat_group')
    topic = models.CharField(max_length=80) #topic mist contains text, image, document, audio, etc
    like_post = models.ManyToManyField(User, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'author_of_chat')
    created_date = models.DateTimeField(auto_now= date.today)
    modified_date = models.DateTimeField(auto_now = datetime.now())


class follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    follow_user = models.ManyToManyField(User, blank=True, related_name='follow_user')