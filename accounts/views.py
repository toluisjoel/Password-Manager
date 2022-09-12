from django.shortcuts import render

from .models import Profile
from .forms import UserRegistrationForm
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


def profile(request):
    context = {}
    return render(request, 'accounts/profile.html', context)

def edit(request):
    pass