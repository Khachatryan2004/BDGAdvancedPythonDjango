from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class CarAdminInline(admin.TabularInline):
    model = Car
    extra = 3
    can_delete = False
    classes = ("collapse",)


@admin.register(Manufacture)
class Manufacture(admin.ModelAdmin):
    list_display = ("id", "name", "email", "created_at")
    list_display_links = ("id", "name")
    list_filter = ("name", "email")
    search_fields = ("name", "email")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [CarAdminInline]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "hp", "position", "created_at", "get_photo", "status")
    list_display_links = ("id", "name", "hp", "position")
    list_filter = ("name", "hp")
    search_fields = ("name", "hp")
    prepopulated_fields = {"slug": ("name",)}
    autocomplete_fields = ("manufacture",)
    readonly_fields = ("get_photo",)
    save_on_top = True
    list_editable = ("status",)
    fieldsets = (
        ("Name and Slug", {
            "fields": (("name", "slug"),)}),
        (None, {
            "fields": ("manufacture", "created_at", "status", "hp")
        })
    )

    def get_photo(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="65" height="40/>"')

    get_photo.short_description = "Nkar"


admin.site.site_title = "Manufacture"
admin.site.site_header = "Car"
