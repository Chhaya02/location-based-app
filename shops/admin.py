from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop
from django.contrib import admin

@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'address','location')