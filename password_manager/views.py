from django.urls import reverse, reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .models import SiteDetail, Website
from .forms import AddPasswordForm, AddSiteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class WebsiteListView(LoginRequiredMixin, generic.ListView):
    model = Website
    context_object_name = 'websites'

    def get_queryset(self):
        return User.objects.get(username=self.request.user).websites.filter(user=self.request.user)


@login_required
def same_password(request):
    user = request.user
    site_details = user.details.all()
    passwords = dict()

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
        weblink_form = AddSiteForm(request.POST)
        password_form = AddPasswordForm(request.POST)

        if weblink_form.is_valid() and password_form.is_valid():
            website_link = weblink_form.save(commit=False)
            site_password = password_form.save(commit=False)

            website_link.user = request.user
            site_password.user = request.user

            try:
                site_password.website = Website.objects.get(
                    user=request.user, website=website_link)
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


class EditPasswordView(LoginRequiredMixin, generic.UpdateView):
    model = SiteDetail
    fields = ('username', 'password')
    template_name = 'password_manager/edit_password.html'
    success_url = reverse_lazy('manager:home')


class DeletePasswordtView(LoginRequiredMixin, generic.DeleteView):
    model = SiteDetail
    template_name = 'password_manager/delete_password.html'
    success_url = reverse_lazy('manager:home')
