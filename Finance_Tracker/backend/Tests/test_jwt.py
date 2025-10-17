from django.urls import reverse
from rest_framework.test import APITestCase, APIClient, force_authenticate
from django.contrib.auth import get_user_model


class AuthenticatedViewTest(APITestCase):
        def setUp(self):
            print("Running test_jwt")
            User = get_user_model()
            self.username = "testuser"
            self.password = "testpassword"
            self.user = User.objects.create_user(username=self.username, password=self.password)
            self.token_url = reverse('token_obtain_pair') # Assuming 'token_obtain_pair' is your URL name

            # Obtain the access token
            response = self.client.post(self.token_url, {'username': self.username, 'password': self.password})
            self.access_token = response.data['access']

        def test_access_protected_view(self):
            # Define the URL of your protected view
            protected_url = reverse('expenseGetView') 

            # Make a request with the Authorization header
            headers = {'HTTP_AUTHORIZATION': f'Bearer {self.access_token}'}
            response = self.client.get(protected_url, **headers)
            self.assertEqual(response.status_code, 200)
            # Add further assertions based on the expected response content
        
        def test_protected(self):
            login_url = reverse('loginView')
            get_url = reverse('expenseGetView')
            response = self.client.post(login_url, {'username': self.username, 'password': self.password})
            login_access_token = response.data['access']
            login_headers = {'HTTP_AUTHORIZATION': f'Bearer {login_access_token}'}
            response = self.client.get(get_url, **login_headers)
            self.assertEqual(response.status_code, 200)