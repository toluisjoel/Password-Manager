from django.db import models
from django.contrib.auth import get_user_model
from .encryption import decrypt


class Website(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='websites')
    link = models.URLField()
    
    # def save(self, *args, **kwargs):
    #     if (self.website).startswith('http://'):
    #         self.website = (self.website).replace('http://', 'https://')
    #     super(Website, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['-link']
        unique_together = 'user', 'link'
    
    def __str__(self):
        return self.link


class SiteDetail(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='details') 
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='details')
    username = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-updated_at',)
        unique_together = 'website', 'username', 'password'
    
    def decrypt_password(self):
        return decrypt(self.password)
    
    def __str__(self):
        return self.username

