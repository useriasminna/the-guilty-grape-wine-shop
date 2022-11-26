"""
Newsletter App - Urls
----------------
Urls for Newsletter App.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.SubscribeToNewsletter.as_view(),
         name='subscribe_to_newsletter'),
]
