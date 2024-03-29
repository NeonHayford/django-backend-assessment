from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# from django.contrib.auth.models import User
from core.settings import AUTH_USER_MODEL

class CustomUserManager(BaseUserManager):
    # pass
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        if not password:
            raise ValueError('Password is required')
        
        user = self.model(
            email = self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        try:
            user = self.create_user(
                email= email,
                password=password,
                **extra_fields
            )
            return user
        except:
            raise ValueError('An Error Occured Please Try Again')
        




class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255)
    username = None
    groups = None
    user_permissions = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        self.full_name = f'{self.first_name} {self.last_name}'
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        # assert self.email == None
        return f"{self.full_name}"

        

class UserProfile(models.Model):
    user= models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='users_profile')
    user_profile = models.ImageField(upload_to='user_profile/%y/%m/%d')
    bio = models.TextField()
    