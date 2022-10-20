"""
Newsletter App - Admin
----------------
Admin Configuration for Newsletter App.
"""
from django.contrib import admin

from newsletter.models import Subscription

# Register your models here.
admin.site.register(Subscription)
