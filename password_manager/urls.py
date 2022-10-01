from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('', views.WebsiteList.as_view(), name='home'),
    path('related-passwords/', views.same_password, name='same_passwords'),
    path('add-password/', views.add_password, name='add_password'),
    path('edit-password/<str:pk>', views.EditPassword.as_view(), name='edit_password'),
    path('delete-password/<str:pk>', views.DeletePassword.as_view(), name='delete_password'),
]