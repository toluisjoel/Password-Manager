from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.home),
    path('', include('django.contrib.auth.urls')),
]