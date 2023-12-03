from django.contrib import admin

from .models import ForAPI


@admin.register(ForAPI)
class ForAPIAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_editable = ('status',)
    list_filter = ('status',)
