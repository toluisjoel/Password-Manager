from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from password_manager.models import Website
from .forms import CustomUserCreationForm, CustomUserChangeForm


class WebsiteInline(admin.TabularInline):
    model = Website
    extra = 1


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
    
    inlines = [WebsiteInline]


admin.site.register(CustomUser, CustomUserAdmin)