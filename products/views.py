"""
Products App - Views
----------------
Views for Products App.
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView
from django.db.models import Q
from django.contrib import messages
from models import Product, Category


class Products(ListView):
    """ A view to show all products, including sorting and search queries """
    template_name = "products/products.html"
    model = Product
    paginate_by = 12
    context_object_name = "products"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['products'] = Product.objects.all()
        return context

    def get(self, request):
        products = Product.objects.all().order_by('style')
        query = None
        category = None
        is_deluxe = None
        deluxe_style = None
        filters = {}
        remove_filter = None

        # CREATE DINAMIC QUERY FOR FILTERING PRODUCTS
        filter_options = ['category', 'style', 'grapes', 'year',
                          'country', 'region', 'food_pairing', 'is_deluxe']
        filter_clauses = {}
        for key, value in request.GET.items():
            if key in filter_options:
                if key == 'category':
                    filter_clauses[key] = get_object_or_404(
                        Category, name=value)
                elif key in ('grapes', 'food_pairing'):
                    filter_clauses[key+"__contains"] = value
                else:
                    filter_clauses[key] = value

        if filter_clauses:
            products = products.filter(**filter_clauses)
            for key, value in filter_clauses.items():
                if key == 'category':
                    category_name = request.GET['category']
                    category = get_object_or_404(Category, name=category_name)
                    # ADD CATEGORY FILTER TO FILTER CONTEXT
                    if 'filter' in request.GET and\
                        request.get_full_path().find('filter') < \
                       request.get_full_path().find('category'):
                        filters['category'] = 'CATEGORY - ' + \
                                              category.get_friendly_name()
                        category = None
                # ADD STYLE FILTER TO FILTER CONTEXT
                elif key == 'style':
                    deluxe_style = request.GET['style']
                    filters['style'] = 'STYLE OF WINE - ' + deluxe_style
                # ADD GRAPE VARIETY FILTER TO FILTER CONTEXT
                elif 'grapes' in key:
                    grape = request.GET['grapes']
                    filters['grapes'] = 'GRAPE VARIETY - ' + grape
                # ADD YEAR FILTER TO FILTER CONTEXT
                elif key == 'year':
                    year = request.GET['year']
                    filters['year'] = 'YEAR - ' + year
                # ADD COUNTRY FILTER TO FILTER CONTEXT
                elif key == 'country':
                    country = request.GET['country']
                    filters['country'] = 'COUNTRY - ' + country
                # ADD REGION FILTER TO FILTER CONTEXT
                elif key == 'region':
                    region = request.GET['region']
                    filters['region'] = 'REGION - ' + region
                # ADD FOOD FILTER TO FILTER CONTEXT
                elif 'food_pairing' in key:
                    food = request.GET['food_pairing']
                    filters['food_pairing'] = 'FOOD PAIRING - ' + food

        # HANDLE SEARCH QUERIES
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(region__icontains=query) | \
                Q(country__icontains=query) | Q(grapes__icontains=query) | \
                Q(style__icontains=query)
            products = products.filter(queries)

        # ADD IS_DELUXE VALUE TO CONTEXT
        if 'is_deluxe' in request.GET:
            deluxe = request.GET['is_deluxe']
            is_deluxe = deluxe

        # ADD FILTERS LISTS TO CONTEXT FOR FILTERS DROPDOWNS
        categories = Category.objects.filter(
            id__in=products.values_list(
                'category', flat=True).distinct()).order_by('name')

        deluxe_styles = products.values_list(
            'style', flat=True).distinct().order_by('style')

        grapes_list = []
        for grapes in products.values_list('grapes', flat=True):
            grapes_values = grapes.split(', ')
            grapes_list.extend(grapes_values)
        grapes_list = [*set(grapes_list)]
        grapes_list.sort()

        years_list = products.values_list(
            'year', flat=True).distinct().order_by('-year')

        regions_list = products.values_list(
            'region', flat=True).distinct().order_by('region')

        countries_list = products.values_list(
            'country', flat=True).distinct().order_by('country')

        food_pairings_list = []
        for food in products.values_list('food_pairing', flat=True):
            food_values = food.split(', ')
            food_pairings_list.extend(food_values)
        food_pairings_list = [*set(food_pairings_list)]
        food_pairings_list.sort()

        # ADD FILTER PARAMETER TO CURRENT URL ONLY ONCE
        current_url = request.get_full_path()
        if '?' in current_url:
            current_url += '&'
        else:
            current_url += '?'
        if 'filter' not in current_url:
            current_url += 'filter=True&'

        # REMOVE FILTERS FROM URL TO BE USED IN TEMPLATE HREFS WHEN
        # 'CLEAR ALL' BUTOTN IS ACTIVE
        current_url_no_filters = request.get_full_path()
        if 'filter' in current_url_no_filters:
            string_index = current_url_no_filters.find('filter=True&')
            current_url_no_filters = current_url_no_filters[0:string_index-1]

        # CHECK IF THERE IS ONLY ONE FILTER APPLIED AND CREATE BOOLEAN VALUE
        # TO BE ADDED TO CONTEXT
        parameters = []
        for key, value in request.GET.items():
            parameters.append(key)
        if parameters:
            if parameters[len(parameters)-2] == 'filter' and \
               parameters[len(parameters)-1] in filter_options:
                remove_filter = True

        context = {
            'products': products,
            'search_term': query,
            'current_category': category,
            'is_deluxe': is_deluxe,
            'categories': categories,
            'deluxe_styles': deluxe_styles,
            'deluxe_style': deluxe_style,
            'filters_list': filters,
            'grapes_list': grapes_list,
            'years_list': years_list,
            'regions_list': regions_list,
            'countries_list': countries_list,
            'food_pairing_list': food_pairings_list,
            'current_url': current_url,
            'current_url_no_filters': current_url_no_filters,
            'remove_filter': remove_filter,
            }
        return render(request, 'products/products.html', context)
