from django.test import TestCase
from django.contrib.auth.models import User
from friendlist.models import Friend
from django.urls import reverse

class HomePageTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class LoginTest(TestCase):
    def test_login_page_status_code(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
    
    # Test with correct credentials
    def test_login_functionality(self):
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/login/', {'username': 'incorrect_username', 'password': 'incorrect_password'})
        # Check if the response contains the error message
        self.assertContains(response, "Invalid username or password", status_code=200)
        

class SearchUserTest(TestCase):
    def test_search_user_page_status_code(self):
        response = self.client.get('/users_search/')
        self.assertEqual(response.status_code, 200)

    def test_search_user_functionality(self):
        response = self.client.get('/users_search/', {'query': 'username'})
        self.assertEqual(response.status_code, 200)

class ProfilePageTest(TestCase):
    def test_create_post(self):
        # Create a user and log in
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Now, make a POST request to create a post
        response = self.client.post('/create_post/', {'caption': 'Test post content'}, format='json')

        # Check if the post was created successfully
        self.assertIn(response.status_code, [200, 302])  # Assuming a successful redirect

class AddFriendTest(TestCase):
    def setUp(self):
        # Create two users
        self.user1 = User.objects.create_user(username='user1', password='testpassword1')
        self.user2 = User.objects.create_user(username='user2', password='testpassword2')

        # Log in user1
        self.client.login(username='user1', password='testpassword1')

    def test_add_friend(self):
        # Make a POST request to send a friend request
        response = self.client.post(reverse('send_friend_request', args=[self.user2.id]))
        print(Friend.objects.all())
    
        self.assertEqual(response.status_code, 200)

