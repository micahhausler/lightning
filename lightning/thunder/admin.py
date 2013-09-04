from django.contrib.admin import ModelAdmin, site

from . import models

class AlbumAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'is_live']
    search_field = ['name', 'summary']

class PhotoAdmin(ModelAdmin):
    list_display = ['title', 'is_live']
    search_field = ['title', 'summary']

site.register(models.Photo, PhotoAdmin)
site.register(models.Album, AlbumAdmin)
