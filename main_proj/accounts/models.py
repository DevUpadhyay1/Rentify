from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

from .managers import CustomUserManager

def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)

class CustomeUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    contact = models.CharField(max_length=20, default='')
    user_profile_pic = models.ImageField(upload_to=user_directory_path, default='images/default.jpeg')


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email