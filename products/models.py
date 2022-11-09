"""
Products App - Models
----------------
Models for Products App.
"""
from django.db import models


class Category(models.Model):
    """Category model"""
    class Meta:
        """Override Meta class"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        """Method that returns category friendly_name"""
        return self.friendly_name


class Product(models.Model):
    """Product model"""
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    is_deluxe = models.BooleanField()
    sku = models.CharField(max_length=254, unique=True)
    name = models.CharField(max_length=254)
    region = models.TextField(max_length=100)
    country = models.TextField(max_length=100)
    grapes = models.TextField(max_length=254)
    year = models.IntegerField()
    style = models.TextField()
    code = models.CharField(max_length=6, unique=True)
    food_pairing = models.TextField(max_length=60)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image = models.ImageField(null=True, blank=True)
    stock = models.IntegerField(default=1000000)

    def __str__(self):
        return str(self.name)
