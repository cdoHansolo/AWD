from django.test import TestCase

class HomePageTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class SearchUserTest(TestCase):
    def test_search_user_page_status_code(self):
        response = self.client.get('/users_search/')
        self.assertEqual(response.status_code, 200)


    def test_search_user_functionality(self):
        response = self.client.get('/users_search/', {'query': 'username'})
        self.assertEqual(response.status_code, 200)
