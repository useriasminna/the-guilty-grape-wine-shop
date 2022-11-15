"""
Bag App - Views
----------------
Views for Bag App.
"""

from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages

from products.models import Product


class Bag(UserPassesTestMixin, TemplateView):
    """A view that will render the bag page template"""
    template_name = 'bag/bag.html'

    def test_func(self):
        if self.request.user.is_authenticated:
            return not self.request.user.is_superuser
        return True


class AddToBag(UserPassesTestMixin, View):
    """A view that add the product and the corresponding quantity to the
    shopping bag"""
    template_name = 'bag/bag.html'

    def post(self, request, product_id):
        """Override post method"""
        product = get_object_or_404(Product, pk=product_id)
        quantity = int(request.POST.get('quantity'))
        current_url = request.POST.get('current_url')
        bag = request.session.get('bag', {})

        if str(product_id) in list(bag.keys()):
            bag[str(product_id)] += quantity
            messages.success(request, f'Updated {product.name} quantity to\
                {bag[str(product_id)]}')
        else:
            bag[product_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')
        request.session['bag'] = bag
        return redirect(current_url)

    def test_func(self):
        if self.request.user.is_authenticated:
            return not self.request.user.is_superuser
        return True
