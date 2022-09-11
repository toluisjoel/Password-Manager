from django.db import models

from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(default='users/default_profile_photo.svg', upload_to='users/%Y/%m/%d/')

# from django.contrib.auth.models import AbstractUser
# class CustomUser(AbstractUser):
#     avatar = models.ImageField(blank=True)

#     def __str__(self):
#         return self.username