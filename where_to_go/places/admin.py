from django.contrib import admin
from django.utils.html import format_html
from .models import Location, Image
from adminsortable2.admin import SortableInlineAdminMixin


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ['image', ]
    fields = ['location', 'image']

    def image_preview(self, obj):
        return obj.image_preview


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    search_fields = ['title', ]
    inlines = [
        PlaceImageInline,
    ]


# class ImagesInline(admin.TabularInline, SortableStackedInline):
#     model = Image
#     readonly_fields = ('image_report',)
#
#     def image_report(self, obj):
#         return format_html('<img src="{url}" width="{width}" height={height} />'.format(
#             url=obj.image.url,
#             width=200,
#             height=200, ))
#
#
# @admin.register(Location)
# class LocationAdmin(SortableAdminBase, admin.ModelAdmin):
#     inlines = [ImagesInline, ]
#
#
# @admin.register(Image)
# class ImagesAdmin(admin.ModelAdmin):
#     fields = ('location', 'image')
