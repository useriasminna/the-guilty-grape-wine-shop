"""
Home App - Tests
----------------
Tests for Home App.
"""


from django.test import TestCase
from django.contrib.auth import get_user_model


class TestViews(TestCase):
    """
    Unit Tests for Home App Views
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

    def test_home_page(self):
        """ Test if home page renders correct page when user is
        authenticated as client user"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_home_page_neauthenticated(self):
        """ Test if home page renders correct page
        without user authentication """
        self.client.logout()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
