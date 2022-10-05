from django.contrib import admin
from django.utils.html import format_html_join, format_html

from .models import Location, Image


class ImagesInline(admin.TabularInline):
    model = Image
    readonly_fields = ('image_report',)

    def image_report(self, instance):
        try:
            result = format_html_join(
                format_html('<br>'),'{}',
                ((line,) for line in instance.images()), ) or format_html(
                "<span class='errors'>I can't imaging this image.</span>")
        except Exception as exc:
            print('8' * 100)
            print(exc)
        return result


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [ImagesInline, ]


@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    fields = ('location', 'image')
