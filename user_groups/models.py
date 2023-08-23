# from django.db import models
# from django.contrib.auth.models import User
# from  core import settings
# from datetime import datetime, date

# # Create your models here.
# class GroupProfile(models.Model):
#     chat_profile = models.ImageField(upload_to='chat_profile/%h.jpg')
#     owner = models.ForeignKey(User, on_delete= models.CASCADE,related_name = 'user_group')

# class Group(models.Model):
#     group_name = models.CharField(max_length=100)
#     description = models.TextField(max_length=300)
#     member= models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='multiple_users')
#     groups = models.ForeignKey(GroupProfile, on_delete=models.CASCADE, related_name = 'group_profile')
#     created_date = models.DateTimeField(auto_now_add=datetime.now())


# class Chat_message(models.Model):
#     community = models.ForeignKey(UserGroup, on_delete=models.CASCADE, related_name='chat_group')
#     content = models.TextField()
#     image = models.ImageField(upload_to='post_images/user_{0}/%m%d%y'.format(User.get_full_name), null=True, blank=True)
#     video = models.FileField(upload_to='post_videos/user_{0}/%m%d%y', null=True, blank=True) #topic mist contains text, image, document, audio, etc
#     like_post = models.ManyToManyField(User, blank=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'author_of_chat')
#     created_date = models.DateTimeField(auto_now= date.today)
#     modified_date = models.DateTimeField(auto_now = datetime.now())

#     @property
#     def image(self):
#         image_data = '{0}'.format(self.image.url)
#         return image_data
#     @property
#     def video(self):
#         video_data = '{0}'.format(self.video.url)
#         return video_data
    
#     def __str__(self):
#         return self.author


# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     chat = models.ForeignKey(Chat_message, on_delete= models.CASCADE)
#     message = models.TextField()
#     image = models.ImageField(upload_to='post_images/user_{0}/%m%d%y'.format(User.get_full_name), null=True, blank=True)
#     video = models.FileField(upload_to='post_videos/user_{0}/%m%d%y', null=True, blank=True)
#     like_post = models.ManyToManyField(User, blank=True)
#     created_date = models.DateTimeField(auto_now_add=True)

#     @property
#     def image(self):
#         image_data = '{0}'.format(self.image.url)
#         return image_data
#     @property
#     def video(self):
#         video_data = '{0}'.format(self.video.url)
#         return video_data


# class Reply(models.Model):
#     chat = models.ForeignKey(Chat_message, on_delete= models.CASCADE)
#     message = models.TextField()
#     image = models.ImageField(upload_to='post_images/user_{0}/%m%d%y'.format(User.get_full_name), null=True, blank=True)
#     video = models.FileField(upload_to='post_videos/user_{0}/%m%d%y', null=True, blank=True)
#     like_post = models.ManyToManyField(User, blank=True)
#     created_date = models.DateTimeField(auto_now_add=True)

#     @property
#     def image(self):
#         image_data = '{0}'.format(self.image.url)
#         return image_data
#     @property
#     def video(self):
#         video_data = '{0}'.format(self.video.url)
#         return video_data