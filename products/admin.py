"""
Products App - Admin
----------------
Admin configuration for Products App.
"""
from django.contrib import admin
from .models import Product, Category
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """Class for displaying products in admin panel"""
    list_display = (
        'sku',
        'name',
        'category',
        'country',
        'year',
        'price',
        'rating',
    )
    readonly_fields = ('rating', )
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """Class for displaying categories in admin panel"""
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
