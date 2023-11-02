from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('categories',)
    list_display_links = ('categories',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('news',)
    list_display_links = ('news',)
