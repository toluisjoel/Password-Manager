from django.shortcuts import render

from .models import Profile
from django.urls import reverse
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from .forms import UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            user_form.save()
            Profile.objects.create(user=new_user)
            context = {'new_user': new_user}
            return render(request, 'accounts/register_done.html', context)
    else:
        user_form = UserRegistrationForm()

    context = {'user_form': user_form}
    return render(request, 'accounts/register.html', context)

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save() and user_form.save()
            
        return redirect(reverse('accounts:profile'))

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'accounts/edit.html', context)

def profile(request):
    context = {}
    return render(request, 'accounts/profile.html', context)