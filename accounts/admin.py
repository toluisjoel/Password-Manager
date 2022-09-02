from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ('username', 'email', 'is_active', 'avatar', 'last_login')
    list_filter = ('last_login', 'is_active')
    search_fields = ('email',)
    
    fieldsets = (
        (None, {
            # 'classes': ('wide',),
            'fields': ('username', 'email', 'avatar', 'is_staff', 'is_active')}
         ),
    )
    
    add_fieldsets = ( 
        (None, {
            # 'classes': ('wide',),
            'fields': ('username', 'email', 'avatar', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )


admin.site.register(CustomUser, CustomUserAdmin)