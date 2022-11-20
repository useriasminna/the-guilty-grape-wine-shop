"""
Wishlist App - Views
----------------
Views for Wishlist App.
"""
import json
import urllib
from django.db.models import F
from django.views.generic import ListView, View
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.db.models import Q
from django.db.models.functions import Lower
from products.models import Category, Product

from wishlist.forms import SetWishlistRelation

from wishlist.models import WishlistLine


class WishList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    A view that provides the wishlist of products
    """
    template_name = "wishlist/wishlist.html"
    model = WishlistLine

    def get(self, request):
        wishlist = Product.objects.filter(
            pk__in=WishlistLine.objects.filter(
                user=self.request.user).values_list('product'))
        query = None
        category = None
        is_deluxe = None
        deluxe_style = None
        filters = {}
        remove_filter = None
        sort = None
        direction = None
        # GET EVERY PRODUCT COUNT OF APPEARENCE IN WISHLISTLINE DATABASE
        wishlist_product_count = []
        products = Product.objects.filter(
            pk__in=WishlistLine.objects.filter(
                user=self.request.user).values_list(
                    'product'))
        for product in products:
            wishlist_product_count.append(
                {
                    'id': product.pk,
                    'count': WishlistLine.objects.filter(
                            product=product).count(),
                })

        # CREATE SORT ORDERING
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                wishlist = wishlist.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            if sortkey != 'best_sellers' and sortkey != 'rating':
                wishlist = wishlist.order_by(sortkey)
            if sortkey == 'rating':
                wishlist = wishlist.order_by(F(sortkey).asc(nulls_last=True))
        if sort == 'best_sellers':
            current_sorting = sort
        else:
            current_sorting = f'{sort}_{direction}'

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
            wishlist = wishlist.filter(**filter_clauses)
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
                return redirect(reverse('wishlist'))

            queries = Q(name__icontains=query) | Q(region__icontains=query) | \
                Q(country__icontains=query) | Q(grapes__icontains=query) | \
                Q(style__icontains=query)
            wishlist = wishlist.filter(queries)

        # ADD IS_DELUXE VALUE TO CONTEXT
        if 'is_deluxe' in request.GET:
            deluxe = request.GET['is_deluxe']
            is_deluxe = deluxe

        # ADD FILTERS LISTS TO CONTEXT FOR FILTERS DROPDOWNS
        categories = Category.objects.filter(
            id__in=wishlist.values_list(
                'category', flat=True).distinct()).order_by('name')

        deluxe_styles = wishlist.values_list(
            'style', flat=True).distinct().order_by('style')

        grapes_list = []
        for grapes in wishlist.values_list('grapes', flat=True):
            grapes_values = grapes.split(', ')
            grapes_list.extend(grapes_values)
        grapes_list = [*set(grapes_list)]
        grapes_list.sort()

        years_list = wishlist.values_list(
            'year', flat=True).distinct().order_by('-year')

        regions_list = wishlist.values_list(
            'region', flat=True).distinct().order_by('region')

        countries_list = wishlist.values_list(
            'country', flat=True).distinct().order_by('country')

        food_pairings_list = []
        for food in wishlist.values_list('food_pairing', flat=True):
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
        # 'CLEAR ALL' BUTTON IS ACTIVE
        current_url_no_filters = request.path_info
        parameters = request.GET.copy()
        parameters_list = json.loads(json.dumps(request.GET)).items()
        is_filter = False
        for key, value in parameters_list:
            if key == 'filter':
                is_filter = True
                del parameters['filter']
            if is_filter is True and key in filter_clauses:
                del parameters[key]
        current_url_no_filters += '?' + urllib.parse.urlencode(parameters)

        # CHECK IF THERE IS ONLY ONE FILTER APPLIED AND CREATE BOOLEAN VALUE
        # TO BE ADDED TO CONTEXT
        parameters = []
        for key, value in request.GET.items():
            parameters.append(key)
        if parameters:
            if parameters[len(parameters)-2] == 'filter' and \
               parameters[len(parameters)-1] in filter_options:
                remove_filter = True
            else:
                for i in range(0, len(parameters)-2):
                    if parameters[i] == 'filter' and \
                       parameters[i+1] in filter_options:
                        one_filter = True
                        for j in range(i+2, len(parameters)):
                            if parameters[j] in filter_options:
                                one_filter = False
                                break
                        if one_filter is True:
                            remove_filter = True

        context = {
            'wishlist': wishlist,
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
            'current_sorting': current_sorting,
            'wishlist_product_count': wishlist_product_count
            }
        return render(request, 'wishlist/wishlist.html', context)

    def test_func(self):
        return not self.request.user.is_superuser


class AddProductToWishList(UserPassesTestMixin, View):
    """
    A view that provides a form for creating a new entry in
    WishlistLine
    """
    def post(self, request, product_id):
        """Override post method"""
        current_url = request.POST.get('current_url')
        wishlist_form = SetWishlistRelation(data=request.POST)

        if wishlist_form.is_valid():
            user = request.user
            product = get_object_or_404(Product, pk=product_id)
            wishlist_form = WishlistLine(user=user, product=product)
            wishlist_form.save()

        return redirect(current_url)

    def get(self, request, product_id, *args, **kwargs):
        """Override get method to redirect to product details page"""
        return redirect('/products/product_details/' + str(product_id))

    def test_func(self):
        return not self.request.user.is_superuser


class RemoveProductFromWishList(LoginRequiredMixin, UserPassesTestMixin,
                                DeleteView):
    """
    A view that deletes a WishlistLine entry from the database.
    The action is performed only if the authenticated user
    is the author of WishlistLine entry.
    """

    model = WishlistLine
    template_name = 'menu.html'

    def get_success_url(self):
        id_key = self.get_object().id
        return redirect('/products/product_details/' + str(id_key))

    def get_object(self):
        return WishlistLine.objects.get(pk=self.kwargs.get('wishlist_id'))

    def get(self, request, *args, **kwargs):
        """Override get method to redirect to product details page"""
        id_key = self.get_object().id
        return redirect('/products/product_details/' + str(id_key))

    def test_func(self):
        item = self.get_object()
        return self.request.user == item.user

    def delete(self, request, *args, **kwargs):
        wishlist_id = self.kwargs['wishlist_id']
        current_url = request.POST.get('current_url')
        wishlist = WishlistLine.objects.get(pk=wishlist_id)
        wishlist.delete()

        return redirect(current_url)
