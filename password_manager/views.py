from django.views import generic
from django.shortcuts import render
from accounts.models import CustomUser
from .models import Website

class WebsiteListView(generic.ListView):
    context_object_name = 'websites'
    template_name = 'main.html'
    
    def get_queryset(self):
        return CustomUser.objects.get(username=self.request.user).websites.filter(user=self.request.user)