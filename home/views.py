"""
Home App - Views
----------------
Views for Home App
"""

from django.views.generic import TemplateView
from django.shortcuts import render

class Home(TemplateView):
    """
    A view to return the index page
    """
    template_name = 'index.html'
    
