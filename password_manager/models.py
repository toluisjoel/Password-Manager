from django.db import models
from django.contrib.auth import get_user_model


class Website(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='websites')
    website = models.URLField()
    
    def __str__(self):
        return self.website


class SiteDetail(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='details') 
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='details')
    username = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-updated_at',)
    
    def __str__(self):
        return self.username
    
