from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit, name='edit_profile'),
    path('', include('django.contrib.auth.urls')),
]