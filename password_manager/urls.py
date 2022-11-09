from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('', views.WebsiteList.as_view(), name='home'),
    path('related-passwords/', views.same_password, name='same_passwords'),
    path('add-password/', views.add_password, name='add_password'),
    path('edit-password/<int:pk>/', views.edit_password, name='edit_password'),
    path('delete-password/<int:pk>/', views.DeletePassword.as_view(), name='delete_password'),
]