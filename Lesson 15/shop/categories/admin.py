from django.contrib import admin

from categories.models import Category, SubCategory


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price')
    list_display_links = ('id', 'name',)
