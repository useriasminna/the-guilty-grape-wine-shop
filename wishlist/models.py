"""
Wishlist App - Models
----------------
Models for Wishlist App.
"""
from django.db import models
from django.conf import settings

from products.models import Product


class WishlistLine(models.Model):
    """Model for WishlistLine object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        to_field='email', blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
