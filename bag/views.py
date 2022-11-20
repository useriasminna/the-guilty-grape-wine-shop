"""
Bag App - Views
----------------
Views for Bag App.
"""

from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, View, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.http import HttpResponse

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
        current_url = request.POST.get('current_url')
        bag = request.session.get('bag', {})
        quantity = request.POST.get('quantity')

        try:
            quantity = int(quantity)
            if quantity in range(1, product.stock+1):
                if str(product_id) in list(bag.keys()):
                    bag[str(product_id)] += quantity
                    messages.success(request, f'Updated <b>{product.name}</b>\
                        quantity to {bag[str(product_id)]}',
                                     extra_tags="bag_add safe")
                else:
                    bag[product_id] = quantity
                    messages.success(request, f'Added <b>{product.name}</b>\
                        to your bag', extra_tags="bag_add safe")
                request.session['bag'] = bag
            elif quantity < 0:
                messages.error(
                    request, f'Quantity input value for <b>{product.name}</b>\
                        cannot be negative',
                    extra_tags='safe')
            else:
                messages.error(
                    request, f'The quantity chosen for <b>{product.name}</b>\
                        exceeds the stock. Please choose a smaller value.',
                    extra_tags='safe')
            return redirect(current_url)
        except Exception as e:
            messages.error(
                    request, f'Quantity input type for <b>{product.name}</b>\
                        is not correct <span hidden>{e}</span>',
                    extra_tags='safe')
            return redirect(current_url)

    def get(self, request, product_id):
        return redirect('/bag/')

    def test_func(self):
        if self.request.user.is_authenticated:
            return not self.request.user.is_superuser
        return True


class RemoveFromBag(UserPassesTestMixin, DeleteView):
    """A view that deletes the product from the shoping bag """
    template_name = 'bag/bag.html'

    def delete(self, request, product_id):
        """Override post method"""
        try:
            product = get_object_or_404(Product, pk=product_id)
            current_url = request.POST.get('current_url')
            bag = request.session.get('bag', {})

            if str(product_id) in list(bag.keys()):
                del bag[str(product_id)]
                messages.success(
                    request, f'<b>{product.name}</b> was removed from\
                     your shopping bag', extra_tags='safe')
            else:
                messages.error(
                    request, f'<b>{product.name}</b> was not found in the\
                     shopping bag. Delete action failed', extra_tags='safe')
            request.session['bag'] = bag
            return redirect(current_url)

        except Exception as e:
            messages.error(request, f'Error removing item: {e}')
            return HttpResponse(status=500)

    def test_func(self):
        if self.request.user.is_authenticated:
            return not self.request.user.is_superuser
        return True


class UpdateBagQuantity(UserPassesTestMixin, View):
    """A view that updates the product quantity"""

    template_name = 'bag/bag.html'

    def post(self, request, product_id):
        """Override post method"""
        product = get_object_or_404(Product, pk=product_id)
        current_url = request.POST.get('current_url')
        bag = request.session.get('bag', {})
        quantity = request.POST.get('quantity')

        try:
            quantity = int(quantity)
            if quantity in range(1, product.stock+1):
                bag[str(product_id)] = quantity
                messages.success(
                    request, f'The quantity for <b>{product.name}</b>\
                     was updated to {bag[str(product_id)]}', extra_tags="safe")
                request.session['bag'] = bag
            elif quantity < 0:
                messages.error(
                    request, f'Quantity input value for <b>{product.name}</b>\
                        cannot be negative',
                    extra_tags='safe')
            else:
                messages.error(
                    request, f'The quantity chosen for <b>{product.name}</b>\
                        exceeds the stock. Please choose a value smaller than\
                            {product.stock}.',
                    extra_tags='safe')
            return redirect(current_url)
        except Exception as e:
            messages.error(
                    request, f'Quantity input type for <b>{product.name}</b>\
                        is not correct <span hidden>{e}</span>',
                    extra_tags='safe')
            return redirect(current_url)

    def test_func(self):
        if self.request.user.is_authenticated:
            return not self.request.user.is_superuser
        return True
