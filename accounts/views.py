from django.shortcuts import render

# Create your views here.

def profile(request):
    context = {}
    return render(request, 'account/profile.html', context)

def edit(request):
    pass