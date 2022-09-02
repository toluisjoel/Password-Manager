from distutils.command.upload import upload
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

class CustomUser(AbstractUser):
    avatar = models.ImageField(blank=True)

    def __str__(self):
        return self.username