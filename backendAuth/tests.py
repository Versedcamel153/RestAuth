from django.test import TestCase
<<<<<<< HEAD

# Create your tests here.
=======
# Create your tests here.

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from allauth.socialaccount.models import SocialAccount
import json
from django.contrib.auth import get_user_model
# Create your tests here.

class AuthTestCase(APITestCase):
    def setUp(self):
    # Create user directly (bypass registration)
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='TestPass123!'
        )


        # Create linked Google account
        SocialAccount.objects.create(
            user=self.user,
            provider='google',
            uid='1234567890',
            extra_data={'email': 'testuser@gmail.com'}
        )

    def test_registration(self):
        url = reverse('rest_register')
        data = {
            'email': 'testemail@gmail.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_with_username(self):
        url = reverse('rest_login')
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertIn('access', response.data)

    def test_login_with_email(self):
        
        url = reverse('rest_login')
        data = {
            'email': 'test@example.com',
            'password': 'TestPass123!',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
>>>>>>> 3ce4b0e (FIxes)
