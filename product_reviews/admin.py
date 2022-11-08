"""
Product Reviews App - Admin
----------------
Models Configuration for Product Reviews App.
"""

from django.contrib import admin
from .models import Review


class ProductReviewAdmin(admin.ModelAdmin):
    """Class for displaying reviews in admin panel"""
    list_display = (
        'pk',
        'rate',
        'review_text',
        'date_created_on',
        'date_updated_on',
        'author',
        'product',
    )


admin.site.register(Review, ProductReviewAdmin)
