from django.db import models
from uuid import uuid5
from core.settings import AUTH_USER_MODEL
from  core import settings
from datetime import datetime, date

# Create your models here.
class Channel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid5)
    Channel_name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    author = models.ForeignKey( AUTH_USER_MODEL, on_delete= models.CASCADE,related_name = 'user_group')
    member= models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='multiple_users')
    created_date = models.DateTimeField(auto_now_add=datetime.now())


class ChannelProfile(models.Model):
    chat_profile = models.ImageField(upload_to='chat_profile/%h.jpg')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name = 'channel_profile')


    def __str__(self):
        return f'{self.channel.author} {self.channel.Channel_name}'
    


class ChannelPost(models.Model):
    channel_content = models.TextField() # watch against the error message
    slug = models.SlugField()
    channel_image = models.ImageField(upload_to='post_images/ch/user_{0}/%m%d%y'.format(AUTH_USER_MODEL.capitalize), null=True, blank=True)
    channel_video = models.FileField(upload_to='post_videos/ch/user_{0}/%m%d%y', null=True, blank=True)
    likes = models.IntegerField(default=0)
    author = models.ForeignKey( AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'author_of_chat')
    created_date = models.DateTimeField(auto_now= date.today)
    modified_date = models.DateTimeField(auto_now = datetime.now())

    @property
    def image(self):
        image_data = '{0}'.format(self.channel_image.url)
        return image_data
    @property
    def video(self):
        video_data = '{0}'.format(self.channel_video.url)
        return video_data
    

class ChannelPostLikes(models.Model):
    post = models.ForeignKey(ChannelPost, on_delete=models.CASCADE, related_name='post_likes')
    like_post = models.ManyToManyField(AUTH_USER_MODEL, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
