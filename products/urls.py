"""
Products App - Urls
----------------
Urls for Products App.
"""
from django.urls import path
from . import views

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
]
