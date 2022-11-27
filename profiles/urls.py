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
    path('order_details/<order_number>/', views.OrderDetails.as_view(),
         name='order_details'),
    path('manage_orders/', views.AdminOrdersList.as_view(),
         name='admin_manage_orders'),
    path('delete_order/<pk>/', views.AdminDeleteOrder.as_view(),
         name='admin_delete_order'),
    path('manage_orders/order_details/<order_number>/',
         views.AdminOrderDetails.as_view(),
         name='admin_order_details'),
]
