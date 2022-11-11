"""
Wishlist App - Admin
----------------
Admin Configuration for Wishlist App.
"""
from django.contrib import admin

from wishlist.models import WishlistLine


class WishlistLineAdmin(admin.ModelAdmin):
    """Class for displaying categories in admin panel"""
    list_display = (
        'user',
        'product',
    )


# Register your models here.
admin.site.register(WishlistLine, WishlistLineAdmin)
