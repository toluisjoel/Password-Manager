from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit, name='edit_profile'),
    path('delete-account/<str:pk>/', views.DeleteAccountView.as_view(), name='delete_account'),
    path('', include('django.contrib.auth.urls')),
]