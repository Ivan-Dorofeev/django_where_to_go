from django.contrib import admin

from .models import Location, Image


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', ]


@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['images']
