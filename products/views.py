"""
Products App - Views
----------------
Views for Products App.
"""
import urllib
import json
from django.db.models import F
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DeleteView, UpdateView, View
from django.urls import reverse_lazy
from django.db.models import Q
from django.db.models.functions import Lower
from django_countries.data import COUNTRIES
from django.contrib import messages
from product_reviews.forms import ReviewForm, UpdateReviewForm
from product_reviews.models import Review as ReviewModel


from products.forms import AddUpdateProductForm
from products.models import Product, Category
from wishlist.forms import SetWishlistRelation
from wishlist.models import WishlistLine


class Products(ListView):
    """ A view to show all products, including sorting and search queries """
    template_name = "products/products.html"
    model = Product
    paginate_by = 12
    context_object_name = "products"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['products'] = Product.objects.all().order_by('style')
        return context

    def get(self, request):
        products = Product.objects.all().order_by('style')
        query = None
        category = None
        is_deluxe = None
        deluxe_style = None
        filters = {}
        remove_filter = None
        sort = None
        direction = None

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            if sortkey != 'best_sellers' and 'rating' not in sortkey:
                products = products.order_by(sortkey)
            elif 'rating' in sortkey:
                if direction == 'asc':
                    products = products.order_by(
                        F('rating').asc(nulls_last=True))
                elif direction == 'desc':
                    products = products.order_by(
                        F('rating').desc(nulls_last=True))

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
                if key not in ('category', 'country', 'grapes',
                               'food_pairing'):
                    filter_clauses[key] = value
                else:
                    if key == 'category':
                        category = get_object_or_404(
                            Category, name=value)
                        filter_clauses[key] = category
                    if key == 'country':
                        country_value = None
                        for c_key, c_value in COUNTRIES.items():
                            if c_value == value:
                                country_value = c_key
                        filter_clauses[key] = country_value
                    if key in ('grapes', 'food_pairing'):
                        filter_clauses[key+"__contains"] = value

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

        countries_list = [COUNTRIES[country_code] for country_code
                          in products.values_list(
                              'country', flat=True).distinct().order_by(
                                  'country')]

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
            'current_sorting': current_sorting,
            }
        return render(request, 'products/products.html', context)


class ProductDetail(ListView):
    """ A view to show a product details including reviews """
    template_name = "products/product_details.html"

    def get(self, request, product_id):
        """Override get method"""
        product = get_object_or_404(Product, pk=product_id)
        current_review = None
        current_wishlist_line = None

        if request.user.is_authenticated and len(
            ReviewModel.objects.filter(
                Q(author=request.user) & Q(product=product))) == 1:
            current_review = ReviewModel.objects.get(
                author=self.request.user, product=product)
        if product.is_deluxe is True:
            update_product_form = AddUpdateProductForm(
                is_deluxe=True, initial={
                    'category': product.category,
                    'country': product.country
                    },
                instance=product, prefix='UPDATE')
        else:
            update_product_form = AddUpdateProductForm(
                instance=product, initial={
                    'category': product.category,
                    'country': product.country
                    },  prefix='UPDATE')

        if self.request.user.is_authenticated and \
            WishlistLine.objects.filter(
                Q(user=self.request.user) & Q(product=product)).exists():
            current_wishlist_line = WishlistLine.objects.get(
                user=self.request.user, product=product)

        add_to_wishlist_form = SetWishlistRelation(data=request.GET)
        context = {
            'product': product,
            'update_product_form': update_product_form,
            'review_form': ReviewForm,
            'update_review_form': UpdateReviewForm(instance=current_review),
            'review_list': ReviewModel.objects.filter(
                product=product).order_by('-date_updated_on'),
            'current_review': current_review,
            'add_to_wishlist_form': add_to_wishlist_form,
            'current_wishlist_line': current_wishlist_line,
        }

        return render(request, 'products/product_detail.html', context)


class ProductAddViewAdmin(LoginRequiredMixin, UserPassesTestMixin, View):
    """
    A view that provides a form to add a new Product entry
    """

    model = Product
    template_name = "base.html"

    fields = [
        'category', 'is_deluxe', 'sku', 'name', 'country', 'region',
        'grapes', 'year', 'style', 'code', 'food_pairing', 'price',
        'image', 'stock']

    def post(self, request):
        """Override post method"""
        form_error = None
        if request.method == 'POST':

            add_product_form = AddUpdateProductForm(
                request.POST, request.FILES, prefix='ADD')

            if add_product_form.is_valid():
                add_product_form.save()
                messages.success(
                    request,
                    'A new product was successfully added to the database')
                return redirect('products')
            else:
                messages.error(
                    request, 'There was a problem when trying to add' +
                             ' a new product to  database. Please try again!')
                return redirect('products')
        else:
            add_product_form = AddUpdateProductForm(request.GET, prefix='ADD')
            context = {
                'form_error': form_error,
            }
        return render(request, 'products.html', context)

    def get(self):
        """Override GET request to redirect to products details page"""
        return redirect('products')

    def test_func(self):
        return self.request.user.is_superuser


class ProductUpdateViewAdmin(LoginRequiredMixin, UserPassesTestMixin,
                             UpdateView):
    """
    A view that provides a form to update the Product entry
    coresponding to the authenticated user
    """

    model = Product
    template_name = "product_detail.html"

    fields = [
        'category', 'is_deluxe', 'sku', 'name', 'country', 'region',
        'grapes', 'year', 'style', 'code', 'food_pairing', 'price',
        'image', 'stock']

    def post(self, request, pk):

        product = get_object_or_404(Product, pk=pk)
        form_error = None
        if request.method == 'POST':

            update_product_form = AddUpdateProductForm(
                request.POST, request.FILES, instance=product,
                prefix='UPDATE')

            if update_product_form.is_valid():
                update_product_form.save()
                messages.success(
                    request, 'Your product was successfully updated')
                return redirect('/products/product_details/' + str(product.pk))
            else:
                messages.error(
                    request, 'There was a problem when trying to update' +
                             'product details. Please try again!')
                return redirect('/products/product_details/'
                                + str(product.pk))
        else:
            update_product_form = AddUpdateProductForm(instance=product,
                                                       prefix='UPDATE')

        context = {
            'update_product_form': update_product_form,
            'product': product,
            'form_error': form_error,
        }

        return render(request, 'product_details.html', context)

    def get_success_url(self):
        id_key = self.get_object().id
        return '/products/product_details/' + str(id_key)

    def get(self, *args, **kwargs):
        """Override GET request to redirect to products details page"""
        return redirect('products')

    def test_func(self):
        return self.request.user.is_superuser


class ProductDeleteViewAdmin(LoginRequiredMixin, UserPassesTestMixin,
                             DeleteView):
    """
    A view that deletes a product entry from the database.
    The action is performed only if the authenticated user
    is an admin.
    """

    model = Product
    success_url = reverse_lazy('products')
    template_name = 'product_detail'
    success_message = "Product was successfully deleted from database."

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, *args, **kwargs):
        """Override GET request to redirect to products page"""
        return redirect('products')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
