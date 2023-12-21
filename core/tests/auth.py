from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.tests import BaseRestTestCase


class AuthTokenTests(BaseRestTestCase):
    def test_authenticate_success(self):
        data = {'username': self.username, 'password': self.password}
        url = reverse('core:auth-token')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_authenticate_failure(self):
        data = {'username': self.username, 'password': 'testpassword'}
        url = reverse('core:auth-token')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
