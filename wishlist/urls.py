"""
Wishlist App - Urls
----------------
Urls for Wishlist App.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.WishList.as_view(), name='wishlist'),
    path('<int:product_id>/add/',
         views.AddProductToWishList.as_view(), name='add_wishlist'),
    path('<int:wishlist_id>/remove/',
         views.RemoveProductFromWishList.as_view(),
         name='remove_wishlist'),
]
