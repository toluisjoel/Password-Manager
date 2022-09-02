from django.shortcuts import render
from .models import Website, WebitePassword
from django.views import generic


class WebsiteList(generic.ListView):
    model = WebitePassword
    context_object_name = 'user_details'
    template_name = 'main.html'
    
    # def get_queryset(self):
    #     # name = Website.objects.filter(self.user_name)
    #     return Website.objects.filter(user_name__iexact='Google')