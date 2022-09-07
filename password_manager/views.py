from itertools import count
from django.views import generic
from django.shortcuts import render
from accounts.models import CustomUser
from .models import SiteDetail, Website
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class WebsiteListView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'websites'
    template_name = 'main.html'
    
    def get_queryset(self):
        return CustomUser.objects.get(username=self.request.user).websites.filter(user=self.request.user)
  
 
@login_required
def same_password(request):
    user = CustomUser.objects.get(username=request.user)
    site_details = user.details.all()
    passwords =  dict()
    
    for details in site_details:
        passwords.setdefault(details.password, []).append([details.username, details.website])
        
    sites_deets = {}
    for password, sites in passwords.items():
        if len(sites) > 1:
            sites_deets.setdefault(password, sites)
    
    context = {
        'sites': sites_deets,
    }
    
    return render(request, 'related_password.html', context)