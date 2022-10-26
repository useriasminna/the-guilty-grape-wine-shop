"""
Products App - Views
----------------
Views for Products App.
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView
from django.db.models import Q
from django.contrib import messages
from .models import Product



class Products(ListView):
    """ A view to show all products, including sorting and search queries """
    template_name = "products/products.html"
    model = Product
    paginate_by = 12
    context_object_name = "products_list"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['products'] = Product.objects.all()
        return context
    
    def get(self, request):
        products = Product.objects.all()
        query = None
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(region__icontains=query) | Q(country__icontains=query) | Q(grapes__icontains=query) | Q(style__icontains=query)
            products = products.filter(queries)
            
        context = {
        'products_list': products,
        'search_term': query,
        }
        return render(request, 'products/products.html', context)
