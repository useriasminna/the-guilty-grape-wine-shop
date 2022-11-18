"""
Checkout App - Views
----------------
Views for Checkout App.
"""

from django.views.generic import TemplateView
from .models import Order
from .forms import OrderForm
# Create your views here.


class Checkout(TemplateView):
    template_name = 'checkout/checkout.html'
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_form'] = OrderForm
        return context
