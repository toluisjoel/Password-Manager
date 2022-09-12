from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('', views.WebsiteListView.as_view(), name='home'),
    path('related-passwords/', views.same_password, name='same_passwords'),
    path('add-password/', views.add_password, name='add_password'),
    path('edit-password/<str:pk>', views.EditPasswordView.as_view(), name='edit_password'),
    path('delete-password/<str:pk>', views.DeletePasswordtView.as_view(), name='delete_password'),
]