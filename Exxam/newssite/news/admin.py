from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", 'created_at', "status")
    list_display_links = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "get_photo", "status")
    list_display_links = ("title",)
    search_fields = ("title", "created_at", "image")
    list_filter = ("created_at", "image")
    readonly_fields = ("get_photo",)
    prepopulated_fields = {"slug": ("title",)}

    def get_photo(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="65" height="40/>"')

    get_photo.short_description = "Photo"
