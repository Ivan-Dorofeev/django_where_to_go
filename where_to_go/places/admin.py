from django.contrib import admin

from .models import Location, Image


class ImagesInline(admin.TabularInline):
    model = Image


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [ImagesInline, ]


@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['images']
