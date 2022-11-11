"""
Products App - Urls
----------------
Urls for Products App.
"""
from django.urls import path
from . import views
from wishlist import views as wishlist_views
urlpatterns = [
    path('', views.Products.as_view(), name='products'),
    path('product/add/',
         views.ProductAddViewAdmin.as_view(), name='product_add'),
    path('product_details/<int:product_id>/', views.ProductDetail.as_view(),
         name='product_detail'),
    path('product_details/<int:pk>/remove/',
         views.ProductDeleteViewAdmin.as_view(),
         name='product_remove_admin'),
    path('product_details/<int:pk>/update/',
         views.ProductUpdateViewAdmin.as_view(), name='product_update'),
    path('product_details/<int:product_id>/wishlist/add',
         wishlist_views.AddProductToWishList.as_view(), name='add_wishlist'),
    path('product_details/<int:product_id>/wishlist/<int:wishlist_id>/remove',
         wishlist_views.RemoveProductFromWishList.as_view(),
         name='remove_wishlist'),
]
