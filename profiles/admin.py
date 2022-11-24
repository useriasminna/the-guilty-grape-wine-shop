"""
Profiles App - Admin
----------------
Admin configuration for Profiles App.
"""
from django.contrib import admin
from .models import UserProfile
# Register your models here.
admin.site.register(UserProfile)
