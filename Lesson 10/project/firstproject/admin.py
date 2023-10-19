from django.contrib import admin

from .models import *


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'hp', 'created_at', 'updated_at')
    list_display_links = ('id', 'brand')
    search_fields = ('brand', 'color')
    list_filter = ('color',)


admin.site.register(Person)


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('color', 'breed', 'animal_owner_number', 'created_at', 'updated_at')
    list_display_links = ('color', 'breed')
    search_fields = ('color', 'breed')
    list_filter = ('color',)


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'product')
    list_display_links = ('nickname',)
    list_filter = ('rating',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_display_links = ('name',)
    list_filter = ('price',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'rating')
    list_display_links = ('reviewer',)
    list_filter = ('reviewer',)


admin.site.register(Flower)


@admin.register(TaxiService)
class TaxiServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'rating')
    list_display_links = ('name',)
    search_fields = ('name', 'city')
    list_filter = ('rating',)


@admin.register(Movie)
class Movie(admin.ModelAdmin):
    list_display = ('title', 'duration', 'rating')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title', 'rating')

