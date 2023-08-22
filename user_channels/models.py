from django.db import models
from uuid import uuid5
from django.contrib.auth.models import User
from  core import settings
from datetime import datetime, date

# Create your models here.
class UserChannel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid5)
    Channel_name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    chat_profile = models.ImageField(upload_to='chat_profile/%h.jpg')
    member= models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='multiple_users')
    owner = models.ForeignKey(User, on_delete= models.CASCADE,related_name = 'user_group')
    created_date = models.DateTimeField(auto_now_add=datetime.now())

class ChannelPost(models.Model):
    channel_content = models.TextField()
    slug = models.SlugField()
    channel_image = models.ImageField(upload_to='post_images/ch/user_{0}/%m%d%y'.format(User.get_full_name), null=True, blank=True)
    channel_video = models.FileField(upload_to='post_videos/ch/user_{0}/%m%d%y', null=True, blank=True)
    like_post = models.ManyToManyField(User, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'author_of_chat')
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
    
