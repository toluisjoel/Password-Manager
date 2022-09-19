from django.views import generic
from .models import SiteDetail, Website
from .encryption import encrypt
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from .forms import AddPasswordForm, AddSiteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class WebsiteListView(LoginRequiredMixin, generic.ListView):
    model = Website
    context_object_name = 'websites'

    def get_queryset(self):
        return Website.objects.filter(user=self.request.user)


@login_required
def same_password(request):
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


class EditPasswordView(LoginRequiredMixin, generic.UpdateView):
    model = SiteDetail
    fields = ('username', 'password')
    template_name = 'password_manager/edit_password.html'
    success_url = reverse_lazy('manager:home')


class DeletePasswordtView(LoginRequiredMixin, generic.DeleteView):
    model = SiteDetail
    template_name = 'password_manager/delete_password.html'
    success_url = reverse_lazy('manager:home')
