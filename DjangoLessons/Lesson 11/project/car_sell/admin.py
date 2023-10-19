from django.contrib import admin
from .models import *


@admin.register(CarSell)
class CarSellAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_of_car', 'currency_choose', 'photo1')
    list_display_links = ('title', 'price_of_car', 'currency_choose')
    list_filter = ('title', 'price_of_car', 'color_of_car', 'color_of_interior', 'comfort1', 'comfort2', 'comfort3',
                   'comfort4', 'comfort5', 'brand', 'year', 'model', 'transmission')

    search_fields = ('title', 'brand', 'model', 'transmission')
