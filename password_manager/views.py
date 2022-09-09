from django.urls import reverse
from django.views import generic
from django.shortcuts import render, redirect
from accounts.models import CustomUser
from .models import SiteDetail, Website
from .forms import AddPasswordForm, AddSiteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class WebsiteListView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'websites'
    
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
    
    return render(request, 'password_manager/related_password.html', context)


@login_required
def add_password(request):
    if request.method == 'POST':
        password_form = AddPasswordForm(request.POST)
        website_form = AddSiteForm(request.POST)

        if password_form.is_valid() and website_form.is_valid():
            website_form.clean()
            new_dets = password_form.save(commit=False)
            new_site = website_form.save(commit=False)
            
            new_dets.user = request.user
            new_site.user = request.user
            new_dets.website = website_form.save()
            
            password_form.save()
            
        return redirect(reverse('manager:home'))

    else:
        password_form = AddPasswordForm()
        website_form = AddSiteForm()

    context = {
        'password_form': password_form,
        'website_form': website_form,
    }
    return render(request, 'password_manager/add_password.html', context)