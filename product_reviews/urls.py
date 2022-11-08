"""
Product Reviews App - Urls
----------------
Urls for Product Reviews App.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('product_details/<int:product_id>/review/add',
         views.AddReview.as_view(), name='add_review'),
    path('product_details/<int:product_id>/review/<int:review_id>/update',
         views.UpdateReview.as_view(), name='update_review'),
]
