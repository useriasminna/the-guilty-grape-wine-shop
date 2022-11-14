"""
Review App - Views
----------------
Views for Review App.
"""
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.db.models import Avg
from products.models import Product
from .forms import ReviewForm, UpdateReviewForm
from .models import Review as ReviewModel


class AddReview(LoginRequiredMixin, UserPassesTestMixin, View):
    """
    A view that creates a new Review entry
    """

    model = ReviewModel
    form_class = ReviewForm
    fields = ['review_text']
    template_name = 'products/product_details'

    def post(self, request, product_id):
        """Override post method"""
        if request.method == 'POST':

            review_form = ReviewForm(data=request.POST)
            product = get_object_or_404(Product, pk=product_id)

            if review_form.is_valid():
                rate = review_form.cleaned_data['rate']
                if rate:
                    rate_value = rate
                else:
                    rate_value = 1
                text = review_form.cleaned_data['review_text']
                user = request.user
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                review = ReviewModel(rate=rate_value, review_text=text,
                                     date_created_on=now, date_updated_on=now,
                                     author=user, product=product)
                review.save()
                messages.success(
                    request, 'Your review was successfully ' +
                             'added to the list.')
                # UPDATE PRODUCT RATE VALUE WITH AVERAGE MEAN OF CORESPONDING
                # REVIEWS RATE VALUES
                product_rates = ReviewModel.objects.filter(
                    product=product)
                product_rates_mean = product_rates.aggregate(
                    Avg('rate'))['rate__avg']
                product.rating = product_rates_mean
                product.save(update_fields=['rating'])

                return HttpResponseRedirect(
                    '/products/product_details/' + str(product_id) +
                    '/#reviewsSection')

            messages.error(
                request,
                'There was a problem submiting your review. ' +
                'Please try again!')
            return HttpResponseRedirect(
                    '/products/product_details/' + str(product_id) +
                    '/#reviewsSection')

        update_review_form = UpdateReviewForm(request.GET)
        review_form = ReviewForm(request.GET)
        return render(
            request,
            '/products/product_details/' + str(product_id) +
            '/#reviewsSection',
            {'review_form': review_form,
             'updare_review_form': update_review_form})

    def test_func(self):
        return not self.request.user.is_superuser


class UpdateReview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view that provides a form to update the Review entry
    coresponding to the authenticated user
    """

    model = ReviewModel
    template_name = 'products/product_details'

    fields = ['rate', 'review_text']

    def post(self, request, product_id, review_id):

        review = get_object_or_404(ReviewModel, pk=review_id)
        if request.method == 'POST':

            update_review_form = UpdateReviewForm(
                data=request.POST, instance=review)
            product = get_object_or_404(Product, pk=product_id)

            if update_review_form.is_valid():
                update_review_form.instance.date_updated_on = datetime.now().\
                    strftime("%Y-%m-%d %H:%M:%S")

                review = ReviewModel()
                update_review_form.save()
                messages.success(
                    request, 'Your review was successfully updated.')

                # UPDATE PRODUCT RATE VALUE WITH AVERAGE MEAN OF CORESPONDING
                # REVIEWS RATE VALUES
                product_rates = ReviewModel.objects.filter(
                    product=product)
                product_rates_mean = product_rates.aggregate(
                    Avg('rate'))['rate__avg']
                product.rating = product_rates_mean
                product.save(update_fields=['rating'])

                return HttpResponseRedirect(
                    '/products/product_details/' + str(product_id) +
                    '/#reviewsSection')

            messages.error(
                request, 'There was a problem when trying to update ' +
                'your review.Please try again!')
            return HttpResponseRedirect(
                    '/products/product_details/' + str(product_id) +
                    '/#reviewsSection')

        review_form = ReviewForm(request.GET)
        return render(request, 'reviews.html',
                      {'review_form': review_form,
                       'update_review_form': update_review_form, })

    def get(self, *args, **kwargs):
        """Override GET request to redirect to reviews"""
        return redirect('products')

    def get_object(self):
        return ReviewModel.objects.get(pk=self.kwargs.get('review_id'))

    def test_func(self):
        item = self.get_object()
        return self.request.user == item.author
