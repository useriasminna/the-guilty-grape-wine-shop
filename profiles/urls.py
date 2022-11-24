"""
Profiles App - Urls
----------------
Urls for Profiles App.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Profile.as_view(),
         name='profile'),
    path('delivery_upate/<user_pk>/',
         views.ProfileDeliveryUpdate.as_view(),
         name='profile_delivery_update'),
    path('order_details/<order_number>', views.OrderDetails.as_view(),
         name='order_details'),
]
