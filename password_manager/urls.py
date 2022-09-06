from django.urls import path
from . import views

urlpatterns = [
    path('', views.WebsiteListView.as_view(), name='home'),
]