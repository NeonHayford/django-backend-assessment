from django.db import models
from core.settings import AUTH_USER_MODEL
# from account.models import CustomUser

# Create your models here.
class Follower(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner')
    following = models.ManyToManyField(AUTH_USER_MODEL, related_name='follow_user')

    def __str__(self):
        return self.user.username