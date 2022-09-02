from turtle import home
from django.urls import path
from . import views

urlpatterns = [
    path('', views.WebsiteList.as_view(), name='home')
]