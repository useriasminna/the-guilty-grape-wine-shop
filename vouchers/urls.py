"""
Vouchers App - Urls
----------------
Urls for Vouchers App.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('voucher_apply/',
         views.UpdateDiscountBag.as_view(),
         name='update_discount'),
]
