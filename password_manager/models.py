from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Website(models.Model):
    website = models.URLField() 
    
    def __str__(self):
        return self.website


# password and detail(username)
class WebitePassword(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='password_details')
    link = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='details')
    
    user_name = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-updated_at',)
    
    def __str__(self):
        return self.user_name
    
