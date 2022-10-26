"""
Products App
----------------
App configuration for Products App.
"""
from django.apps import AppConfig

class ProductsConfig(AppConfig):
    """Product App Configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
