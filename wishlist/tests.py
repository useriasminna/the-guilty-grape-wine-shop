"""
Wishlist App - Tests
----------------
Tests for Wishlist App.
"""


from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from products.models import Product, Category
from wishlist.models import WishlistLine as Wishlist


class TestViews(TestCase):
    """
    Unit Tests for Wishlist App
    """

    def setUp(self):
        """ Create test login """

        # creates test user
        email = "testuser@yahoo.com"
        first = "test"
        last = "user"
        pswd = "T12345678."
        user_model = get_user_model()
        self.user = user_model.objects.create_user(
            email=email, first_name=first, last_name=last, password=pswd)
        logged_in = self.client.login(email=email, password=pswd)
        self.assertTrue(logged_in)

        # creates test category object
        self.category = Category.objects.create(
            name="red_wines",
            friendly_name="Red Wines",
        )

        # creates test product object
        self.product = Product.objects.create(
            category=self.category,
            is_deluxe=False,
            sku='wre10778',
            name='Flor de Crasto',
            region='Douro',
            country='PT',
            grapes='Tinta Roriz, Touriga Franca, Touriga Nacional,\
            Vinhas Velhas',
            year='2019',
            style='Red',
            code='10778',
            food_pairing='Spicy Food, Pasta and Pizza, Hard Cheese',
            price=15.10,
            image='red10778.webp',
            stock=100,
        )

    def test_wishlist_page(self):
        """ Test if products page renders correct page when user is
        authenticated as client user"""
        response = self.client.get('/wishlist/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wishlist/wishlist.html')

    def test_wishlist_page_neauthenticated(self):
        """ Test if wishlist page redirects to login page
        without user authentication """
        self.client.logout()
        response = self.client.get('/wishlist/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response['location'])

    def test_wishlist_context(self):
        """ Test if context is rendered to create wishlist page"""
        response = self.client.get('/wishlist/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('wishlist' in response.context)
        self.assertTrue('search_term' in response.context)
        self.assertTrue('current_category' in response.context)
        self.assertTrue('is_deluxe' in response.context)
        self.assertTrue('categories' in response.context)
        self.assertTrue('deluxe_styles' in response.context)
        self.assertTrue('deluxe_style' in response.context)
        self.assertTrue('filters_list' in response.context)
        self.assertTrue('grapes_list' in response.context)
        self.assertTrue('years_list' in response.context)
        self.assertTrue('regions_list' in response.context)
        self.assertTrue('countries_list' in response.context)
        self.assertTrue('food_pairing_list' in response.context)
        self.assertTrue('current_url' in response.context)
        self.assertTrue('current_url_no_filters' in response.context)
        self.assertTrue('remove_filter' in response.context)
        self.assertTrue('current_sorting' in response.context)
        self.assertTrue('wishlist_product_count' in response.context)

    def test_add_to_wishlist(self):
        """ Test AddProductToWishList view"""
        self.client.login(email='testuser@yahoo.com', password='T12345678.')

        self.assertTrue(Wishlist.objects.all().count, 0)

        self.client.post(reverse('add_wishlist',
                                 kwargs={'product_id': self.product.pk}),
                         {'current_url': '/products/'})

        # Test if object has been added to database after form submit
        self.assertTrue(Wishlist.objects.all().count, 1)

        # Get wishlist object
        wishlist = Wishlist.objects.get(user=self.user, product=self.product)

        # Test context in wishlist page
        response = self.client.get('/wishlist/')
        self.assertTrue('wishlist' in response.context)
        self.assertTrue(len(response.context['wishlist']), 1)
        self.assertTrue(response.context['wishlist'], wishlist)

    def test_remove_from_wishlist(self):
        """ Test RemoveProductFromWishList view"""
        self.client.login(email='testuser@yahoo.com', password='T12345678.')

        self.client.post(reverse('add_wishlist',
                                 kwargs={'product_id': self.product.pk}),
                         {'current_url': '/products/'})

        # Test if object has been added to database after form submit
        self.assertTrue(Wishlist.objects.all().count, 1)

        # Get wishlist object
        wishlist = Wishlist.objects.get(user=self.user, product=self.product)

        self.client.post(reverse('remove_wishlist',
                                 kwargs={'wishlist_id': wishlist.pk}),
                         {'current_url': '/products/'})

        # Test if object has been deleted from database after form submit
        self.assertTrue(Wishlist.objects.all().count, 0)

        # Test context in wishlist page
        response = self.client.get('/wishlist/')
        self.assertTrue('wishlist' in response.context)
        self.assertEqual(len(response.context['wishlist']), 0)
