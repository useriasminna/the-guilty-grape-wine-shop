"""
Product Review App - Apps
----------------
App Configuration for Product Review App.
"""

from django.apps import AppConfig


class ProductReviewsConfig(AppConfig):
    """App configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product_reviews'
