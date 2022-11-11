"""
Wishlist App - Urls
----------------
Urls for Wishlist App.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.WishList.as_view(), name='wishlist'),
]
