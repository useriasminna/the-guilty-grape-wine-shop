"""
Home App - Views
----------------
Views for Home App
"""

from django.views.generic import TemplateView


class Home(TemplateView):
    """
    A view to return the index page
    """
    template_name = 'home/index.html'
