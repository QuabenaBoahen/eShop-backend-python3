from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
 list_display = ['productName', 'productLiveStatus']

@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
 pass


