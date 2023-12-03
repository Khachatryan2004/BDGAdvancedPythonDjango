from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(CarSell)
class CarSellAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_of_car', 'currency_choose', 'get_photo')
    list_display_links = ('title', 'price_of_car', 'currency_choose')
    list_filter = ('title', 'price_of_car', 'color_of_car', 'color_of_interior', 'comfort1', 'comfort2', 'comfort3',
                   'comfort4', 'comfort5', 'brand', 'year', 'model', 'transmission')
    search_fields = ('title', 'brand', 'model', 'transmission')
    save_on_top = True
    fieldsets = (
        ('Title', {
            'fields': (('title'),)
        }),
        ('The type of announcement', {
            'fields': (('publication_type1', 'publication_type2'),)
        }),
        ('Your Status', {
            'fields': (('status1', 'status2'),)
        }),
        ('Characteristics', {
            'fields': (
                ('brand'),
                ('model'),
                ('year'),
                ('engine'),
                ('volumes', 'horsepower'),
                ('transmission', 'unit'),
                ('mileage'),
                ('mileage_type_choose')
            )
        }),
        ('Exterior', {
            'fields': (
                ('color_of_car'),
                ('wheel_size')
            )
        }),
        ('Interior', {
            'fields': (
                ('color_of_interior'),
                ('comfort1'),
                ('comfort2'),
                ('comfort3'),
                ('comfort4'),
                ('comfort5')
            )
        }),
        ('Car Price', {
            'fields': (
                ('price_of_car', 'currency_choose'),
            )
        }),
        ('Detailed information', {
            'fields': (
                ('description'),
                ('photo1'),
                ('photo2', 'photo3', 'photo4', 'photo5', 'photo6')
            )
        }),
        ('Contact Information', {
            'fields': (
                ('mail'),
                ('telephone_number'),
            )
        })
    )

    def get_photo(self, obj):
        if obj.photo1:
            return mark_safe(f"<img src={obj.photo1.url} width='100' height='80'")
        return "No Photo"

    get_photo.short_description = 'Photo'


admin.site.site_title = 'Selling'
admin.site.site_header = 'Selling'
