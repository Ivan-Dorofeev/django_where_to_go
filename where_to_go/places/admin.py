from django.contrib import admin
from django.utils.html import format_html_join, format_html
from django.utils.safestring import mark_safe

from .models import Location, Image


class ImagesInline(admin.TabularInline):
    model = Image
    readonly_fields = ('image_report',)

    def image_report(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=f'where_to_go/media{obj.images.url}',
            width=200,
            height=200,
        )
        )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [ImagesInline, ]


@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    fields = ('location', 'image')
