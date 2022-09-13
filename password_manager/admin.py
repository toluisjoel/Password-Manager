from django.contrib import admin
from .models import Website, SiteDetail

# Register your models here.


class SiteDetailline(admin.TabularInline):
    model = SiteDetail
    extra = 1


class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('user', 'link',)
    search_fields = ('link',)
    inlines = [SiteDetailline]


admin.site.register(Website, WebsiteAdmin)
