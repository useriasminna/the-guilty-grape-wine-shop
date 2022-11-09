
"""
Custom Storages Configuration
"""

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """Set static files location"""
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """Set media files location"""
    location = settings.MEDIAFILES_LOCATION
