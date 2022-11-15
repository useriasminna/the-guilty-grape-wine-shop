"""
Bag App - Urls
----------------
Urls for Bag App.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Bag.as_view(), name='bag'),
    path('add/<int:product_id>/', views.AddToBag.as_view(), name='add_to_bag'),
    path('remove/<int:product_id>/', views.RemoveFromBag.as_view(),
         name='remove_from_bag')
]
