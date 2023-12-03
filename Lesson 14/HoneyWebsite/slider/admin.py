from django.contrib import admin
from .models import *


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title1',)
    list_display_links = ('title1',)
