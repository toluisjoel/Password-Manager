from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('', views.WebsiteListView.as_view(), name='home'),
    path('add-password/', views.add_password, name='add_password'),
    path('related-passwords/', views.same_password, name='same_passwords'),
]