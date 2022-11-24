"""
Profiles App - Views
----------------
Views for Profiles App.
"""
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from checkout.models import Order
from users.models import User


class Profile(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    """A view for rendering user profile page with delivery form
    and orders history"""

    template_name = "profiles/profile.html"
    model = UserProfile

    def get(self, request):
        profile = get_object_or_404(UserProfile, user=request.user)

        form = UserProfileForm(instance=profile)
        orders = Order.objects.filter(user=profile)

        template = 'profiles/profile.html'
        context = {
            'delivery_details_form': form,
            'orders': orders,
        }

        return render(request, template, context)

    def test_func(self):
        return not self.request.user.is_superuser


class ProfileDeliveryUpdate(LoginRequiredMixin, UserPassesTestMixin,
                            UpdateView):
    """A view for updating delivery details for current user"""
    template_name = "profiles/profile.html"
    model = UserProfile

    def post(self, request, user_pk):
        print(user_pk)
        profile = get_object_or_404(UserProfile, user=user_pk)
        orders = Order.objects.filter(user=profile)
        if request.method == 'POST':
            delivery_details_form = UserProfileForm(request.POST,
                                                    instance=profile)
            if delivery_details_form.is_valid():
                delivery_details_form.save()
                messages.success(request, 'Delivery details updated\
                    successfully')

        delivery_details_form = UserProfileForm(instance=profile)

        template = 'profiles/profile.html'
        context = {
            'delivery_details_form': delivery_details_form,
            'orders': orders,
        }

        return render(request, template, context)

    def test_func(self):
        user = User.objects.get(pk=self.kwargs['user_pk'])
        return self.request.user == user


class OrderDetails(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    """A view for rendering order details page"""
    template_name = "checkout/checkout_success.html"

    def get(self, request, order_number):
        order = get_object_or_404(Order, order_number=order_number)

        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
            'from_profile': True,
        }

        return render(request, template, context)

    def test_func(self):
        order = Order.objects.get(order_number=self.kwargs['order_number'])
        user_not_admin = not self.request.user.is_superuser
        return user_not_admin and order.user.user == self.request.user
