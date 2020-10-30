from django.contrib import admin
from . models import Urls


# Register your models here.

class AdminViewUrls(admin.ModelAdmin):
    '''Admin View for '''

    list_display =['id','long_url','short_url','total_hits','created_at']
    ordering = ['id']

admin.site.register(Urls, AdminViewUrls)