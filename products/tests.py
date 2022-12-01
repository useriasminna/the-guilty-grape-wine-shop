"""
Product Reviews App - Tests
----------------
Tests for Product Reviews App.
"""


from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.urls import reverse
from products.models import Product, Category
from products.forms import AddUpdateProductForm


class TestViews(TestCase):
    """
    Unit Tests for Products App
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

    def test_products_page(self):
        """ Test if products page renders correct page when user is
        authenticated as client user"""
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_products_page_neauthenticated(self):
        """ Test if products page renders correct page
        without user authentication """
        self.client.logout()
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_products_context(self):
        """ Test if context is rendered to create products page"""
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('products' in response.context)
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

    def test_product_detail_page(self):
        """ Test if product detail page renders correct template when user is
        authenticated as client user"""
        response = self.client.get(
            '/products/product_details/' + str(self.product.id) + '/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_product_detail_page_neauthenticated(self):
        """ Test if product detail page renders correct template
        without user authentication """
        self.client.logout()
        response = self.client.get(
            '/products/product_details/' + str(self.product.id) + '/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_product_detail_page_context(self):
        """ Test if context is rendered to create products page"""
        response = self.client.get(
            '/products/product_details/' + str(self.product.id) + '/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('product' in response.context)
        self.assertTrue('update_product_form' in response.context)
        self.assertTrue('review_form' in response.context)
        self.assertTrue('update_review_form' in response.context)
        self.assertTrue('review_list' in response.context)
        self.assertTrue('current_review' in response.context)
        self.assertTrue('add_to_wishlist_form' in response.context)
        self.assertTrue('current_wishlist_line' in response.context)

    def test_product_add_for_user_not_superuser(self):
        """ Test if post method for add product fails
        for not admin users"""
        new_product = {
            'ADD-category': self.category.id,
            'ADD-is_deluxe': False,
            'ADD-sku': 'wre10193',
            'ADD-name': 'Rondan Crianza',
            'ADD-region': 'Rioja',
            'ADD-country': 'ES',
            'ADD-grapes': 'Tempranillo',
            'ADD-year': 2018,
            'ADD-style': 'Red',
            'ADD-code': '10193',
            'ADD-food_pairing': 'Spicy Food, Pasta and Pizza, Hard Cheese',
            'ADD-price': 16.45,
            'ADD-image': 'red10193.webp',
            'ADD-stock': 100
        }

        # Call post method for client use
        response = self.client.post(
            reverse('product_add'),
            new_product,)
        # Test if the user gets 403 forbidden on post
        self.assertEqual(response.status_code, 403)

        self.client.logout()
        # Call post method for neauthenticated user
        response = self.client.post(
            reverse('product_add'),
            new_product)
        # Test if the neauthenticated user is redirected to login page
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response['location'])

    def test_product_add_admin(self):
        """Test ProductAddViewAdmin view"""

        self.client.login(email='testuser@yahoo.com', password='T12345678.')
        # Set user as admin
        self.user.is_staff = True
        self.user.is_admin = True
        self.user.save()

        new_product = {
            'ADD-category': self.category.id,
            'ADD-is_deluxe': False,
            'ADD-sku': 'wre10193',
            'ADD-name': 'Rondan Crianza',
            'ADD-region': 'Rioja',
            'ADD-country': 'ES',
            'ADD-grapes': 'Tempranillo',
            'ADD-year': 2018,
            'ADD-style': 'Red',
            'ADD-code': '10193',
            'ADD-food_pairing': 'Spicy Food, Pasta and Pizza, Hard Cheese',
            'ADD-price': 16.45,
            'ADD-image': 'red10193.webp',
            'ADD-stock': 100
        }
        # Test if form is valid
        form = AddUpdateProductForm(new_product, prefix='ADD')
        self.assertTrue(form.is_valid(), form.errors)
        # Call post method for ProductAddViewAdmin view
        response = self.client.post(reverse('product_add'), new_product)

        messages = list(get_messages(response.wsgi_request))
        # Test if a message was added to list
        self.assertEqual(len(messages), 1)
        # Test if 'success' is in message tags
        self.assertIn('success', messages[0].tags)
        # Test if post method redirects to correct page
        self.assertEqual(response.status_code, 302)
        self.assertEqual('/products/', response['location'])

    def test_product_update_for_user_not_superuser(self):
        """ Test if post method for update product fails
        for not admin users"""
        update_product = {
            'UPDATE-category': self.category.id,
            'UPDATE-is_deluxe': False,
            'UPDATE-sku': 'wre10778',
            'UPDATE-name': 'Flor de Crasto',
            'UPDATE-region': 'Douro',
            'UPDATE-country': 'PT',
            'UPDATE-grapes': 'Tinta Roriz, Touriga Franca, Touriga Nacional,\
            Vinhas Velhas',
            'UPDATE-year': '2019',
            'UPDATE-style': 'Red',
            'UPDATE-code': '10778',
            'UPDATE-food_pairing': 'Spicy Food, Pasta and Pizza, Hard Cheese',
            'UPDATE-price': 15.10,
            'UPDATE-image': 'red10778.webp',
            'UPDATE-stock': 900,
        }

        # Call post method for client use
        response = self.client.post(reverse('product_update',
                                            kwargs={'pk': self.product.id, }),
                                    update_product)
        # Test if the user gets 403 forbidden on post
        self.assertEqual(response.status_code, 403)

        self.client.logout()
        # Call post method for neauthenticated user
        response = self.client.post(reverse('product_update',
                                            kwargs={'pk': self.product.id, }),
                                    update_product)
        # Test if the neauthenticated user is redirected to login page
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response['location'])

    def test_product_update_admin(self):
        """Test ProductUpdateViewAdmin view"""

        self.client.login(email='testuser@yahoo.com', password='T12345678.')
        # Set user as admin
        self.user.is_staff = True
        self.user.is_admin = True
        self.user.save()

        update_product = {
            'UPDATE-category': self.category.id,
            'UPDATE-is_deluxe': False,
            'UPDATE-sku': 'wre10778',
            'UPDATE-name': 'Flor de Crasto',
            'UPDATE-region': 'Douro',
            'UPDATE-country': 'PT',
            'UPDATE-grapes': 'Tinta Roriz, Touriga Franca, Touriga Nacional,\
            Vinhas Velhas',
            'UPDATE-year': '2019',
            'UPDATE-style': 'Red',
            'UPDATE-code': '10778',
            'UPDATE-food_pairing': 'Spicy Food, Pasta and Pizza, Hard Cheese',
            'UPDATE-price': 15.10,
            'UPDATE-image': 'red10778.webp',
            'UPDATE-stock': 900,
        }

        form = AddUpdateProductForm(
            update_product, instance=self.product, prefix='UPDATE')
        # Test if form is valid
        self.assertTrue(form.is_valid(), form.errors)
        # Call post method for ProductUpdateViewAdmin view
        response = self.client.post(reverse('product_update',
                                            kwargs={'pk': self.product.id, }),
                                    update_product)
        # Test if product stock value has been updated
        self.assertEqual(self.product.stock, 900)
        # Test if post method redirects to correct page
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            '/products/product_details/' + str(self.product.id),
            response['location'])
