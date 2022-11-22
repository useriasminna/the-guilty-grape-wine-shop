"""
Products App - Models
----------------
Models for Products App.
"""
from django.db import models
from django_countries.fields import CountryField


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
    name = models.CharField(max_length=254, null=False, blank=False)
    region = models.CharField(max_length=100, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    grapes = models.CharField(max_length=254, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    style = models.CharField(max_length=50, null=False, blank=False)
    code = models.CharField(max_length=6, unique=True)
    food_pairing = models.CharField(max_length=254, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False,
                                blank=False)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image = models.ImageField(null=True, blank=True)
    stock = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return str(self.name)
