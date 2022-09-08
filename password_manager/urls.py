from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('', views.WebsiteListView.as_view(), name='home'),
    path('related-passwords/', views.same_password, name='same_passwords'),
]