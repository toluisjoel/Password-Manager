from django.contrib import admin

from password_manager.models import Website

class WebsiteInline(admin.TabularInline):
    model = Website
    extra = 1

# from .models import CustomUser
# from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationForm, CustomUserChangeForm


# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
    
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm

#     list_display = ('username', 'email', 'is_active', 'avatar', 'last_login')
#     list_filter = ('last_login', 'is_active')
#     search_fields = ('email',)
    
#     fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': 
#                 (
#                     'username','password', 'first_name', 'last_name', 'email', 'avatar', 'is_active',
#                     'is_staff', 'is_superuser', 'groups', 'user_permissions', 'last_login', 'date_joined',
#                     )
#                 }
#          ),
#     )
    
#     add_fieldsets = ( 
#         (None, {
#             # 'classes': ('wide',),
#             'fields': ('username', 'email', 'avatar', 'password1', 'password2')}
#          ),
#     )
    
#     inlines = [WebsiteInline]


# admin.site.register(CustomUser, CustomUserAdmin)