from django.db import models
from  core.settings import AUTH_USER_MODEL
from datetime import datetime
from uuid import uuid4

# Create your models here.
class Group(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    group_name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    member= models.ManyToManyField(AUTH_USER_MODEL, related_name='group_multiple_users')
    chat_profile = models.ImageField(upload_to='chat_profile/%h.jpg')
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete= models.CASCADE,related_name = 'user_group')
    created_at = models.DateTimeField(auto_now_add=datetime.now())
    updated_at = models.DateTimeField(auto_now=True)


class ChatMessage(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    community = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='chat_group')
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/user_{0}/%m%d%y'.format(AUTH_USER_MODEL.join('cmimg')), null=True, blank=True)
    video = models.FileField(upload_to='post_videos/user_{0}/%m%d%y'.format(AUTH_USER_MODEL.join('cmvid')), null=True, blank=True) #topic mist contains text, image, document, audio, etc
    like_post = models.ManyToManyField(AUTH_USER_MODEL, blank=True)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'author_of_group_chat')
    created_date = models.DateTimeField(auto_now_add= datetime.now())

    @property
    def image(self):
        image_data = '{0}'.format(self.image.url)
        return image_data
    @property
    def video(self):
        video_data = '{0}'.format(self.video.url)
        return video_data
    
    def __str__(self):
        return self.author


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments_author')
    chat = models.ForeignKey(ChatMessage, on_delete= models.CASCADE)
    message = models.TextField()
    image = models.ImageField(upload_to='post_images/user_{0}/%m%d%y/comment'.format(AUTH_USER_MODEL.join('cmimg')), null=True, blank=True)
    video = models.FileField(upload_to='post_videos/user_{0}/%m%d%y/comment'.format(AUTH_USER_MODEL.join('cmvid')), null=True, blank=True)
    like_post = models.ManyToManyField(AUTH_USER_MODEL, blank=True, related_name='group_comment_likes')
    created_date = models.DateTimeField(auto_now_add=True)

    @property
    def image(self):
        image_data = '{0}'.format(self.image.url)
        return image_data
    @property
    def video(self):
        video_data = '{0}'.format(self.video.url)
        return video_data


class Reply(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    chat = models.ForeignKey(ChatMessage, on_delete= models.CASCADE)
    message = models.TextField()
    image = models.ImageField(upload_to='post_images/user_{0}/%m%d%y/reply'.format(AUTH_USER_MODEL.join('cmimg')), null=True, blank=True)
    video = models.FileField(upload_to='post_videos/user_{0}/%m%d%y/reply'.format(AUTH_USER_MODEL.join('cmvid')), null=True, blank=True)
    like_post = models.ManyToManyField(AUTH_USER_MODEL, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    @property
    def image(self):
        image_data = '{0}'.format(self.image.url)
        return image_data
    @property
    def video(self):
        video_data = '{0}'.format(self.video.url)
        return video_data