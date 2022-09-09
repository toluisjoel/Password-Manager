from django.contrib import admin
from .models import Website, SiteDetail

# Register your models here.

class SiteDetailline(admin.TabularInline):
    model = SiteDetail
    extra = 1

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('user', 'website',)
    search_fields = ('website',)
    inlines = [SiteDetailline]


class SiteDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'username', 'website', 'updated_at')


admin.site.register(Website, WebsiteAdmin)
admin.site.register(SiteDetail ,SiteDetailsAdmin)
