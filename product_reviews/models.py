"""
Product Reviews App - Models
----------------
Models for Product Reviews App.
"""
import datetime
from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db.models import Avg

from users.models import User
from products.models import Product


class Review(models.Model):
    """Model for Product Review Post"""
    rate = models.PositiveSmallIntegerField()
    review_text = models.TextField()
    now = datetime.datetime.now()
    date_created_on = models.DateTimeField(
        default=now.strftime("%Y-%m-%d %H:%M:%S"))
    date_updated_on = models.DateTimeField(
        default=now.strftime("%Y-%m-%d %H:%M:%S"))
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        to_field='email', blank=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=True)

    class Meta:
        """Override Meta method"""
        ordering = ["date_updated_on"]

    def __str__(self):
        return f"Review {self.review_text} by {self.author}"

    @receiver(post_delete, sender=User)
    def update_product_rate_on_user_delete(sender, instance, using, **kwargs):
        """Update each product rate value with average mean of
        corresponding reviews rate values when a user is deleted"""

        for product in Product.objects.all():

            product_rates = Review.objects.filter(product=product)
            product_rates_mean = product_rates.aggregate(
                Avg('rate'))['rate__avg']
            product.rating = product_rates_mean
            product.save(update_fields=['rating'])
