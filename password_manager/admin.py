from django.contrib import admin
from .models import Website, WebitePassword

# Register your models here.


class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('website',)


class WebitePasswordAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_name', 'link', 'updated_at')


admin.site.register(Website, WebsiteAdmin)
admin.site.register(WebitePassword ,WebitePasswordAdmin)
