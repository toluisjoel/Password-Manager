from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from .encryption import encrypt
from .forms import AddPasswordForm, AddSiteForm
from .models import SiteDetail, Website


class WebsiteList(LoginRequiredMixin, generic.ListView):
    model = Website
    context_object_name = 'websites'

    def get_queryset(self):
        """
        Return website only if website has details,
        and delete those without details.
        """
        websites = Website.objects.filter(user=self.request.users)
        websites_with_details = []
        for website in websites:
            website_details = website.details.all()
            if website_details.count() > 0:
                websites_with_details.append(website.id)
            else:
                Website.objects.get(id=website.id).delete()

        return Website.objects.filter(id__in=websites_with_details)


class EditPassword(LoginRequiredMixin, generic.UpdateView):
    model = SiteDetail
    fields = ('username', 'password')
    template_name = 'password_manager/edit_password.html'
    success_url = reverse_lazy('manager:home')


class DeletePassword(LoginRequiredMixin, generic.DeleteView):
    model = SiteDetail
    template_name = 'password_manager/delete_password.html'
    success_url = reverse_lazy('manager:home')


@login_required
def same_password(request):
    """
    accounts with same password
    """    
    user = request.user
    site_password = user.details.all()
    passwords = {}

    for details in site_password:
        passwords.setdefault(details.password, []).append([details.username, details.website])

    same_password = {}
    for password, sites in passwords.items():
        if len(sites) > 1:
            same_password.setdefault(password, sites)

    context = {
        'sites': same_password,
    }

    return render(request, 'password_manager/related_password.html', context)


@login_required
def add_password(request):
    if request.method == 'POST':
        weblink_form = AddSiteForm(request.POST)
        password_form = AddPasswordForm(request.POST)

        if weblink_form.is_valid() and password_form.is_valid():
            website_link = weblink_form.save(commit=False)
            site_password = password_form.save(commit=False)

            website_link.user = request.user
            site_password.user = request.user
            site_password.password = encrypt(site_password.password)

            try:
                site_password.website = Website.objects.get(user=request.user, link=website_link)
            except:
                site_password.website = weblink_form.save()

            site_password.save()

        return redirect(reverse('manager:home'))

    else:
        weblink_form = AddSiteForm()
        password_form = AddPasswordForm()

    context = {
        'weblink_form': weblink_form,
        'password_form': password_form,
    }
    return render(request, 'password_manager/add_password.html', context)
