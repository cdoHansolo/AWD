from django.test import TestCase

# Create your tests here.
# friendlist/tests.py

from django.test import TestCase
from django.urls import reverse

class FriendlistViewsTests(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'friendlist/homepage.html')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'friendlist/loginpage.html')

        # You can add more specific tests for login view if needed.

    # Add more tests for other views as needed...

    def test_invalid_url(self):
        response = self.client.get('/invalid_url/')
        self.assertEqual(response.status_code, 404)
