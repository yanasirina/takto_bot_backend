from django.urls import reverse
from rest_framework import status

from core.tests.base import BaseRestTestCase
from core import factories, models


class User(BaseRestTestCase):
    any_permissions = ['auth.view_user', 'auth.add_user', 'auth.change_user', 'auth.delete_user']

    def generate_data(self):
        factories.User.create_batch(4)

    def test_list(self):
        response = self.client.get(path=reverse('core:users-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_users = models.DjangoUser.objects.order_by('last_name', 'first_name', 'username')
        actual_ids = list(map(lambda user: user['id'], response.data['results']))
        expected_ids = list(expected_users.values_list('id', flat=True))
        self.assertEqual(expected_ids, actual_ids)

        first_course = expected_users.first()
        first_result = response.data['results'][0]
        self.assertEqual(first_result['id'], first_course.id)
        self.assertEqual(first_result['username'], first_course.username)
        self.assertEqual(first_result['first_name'], first_course.first_name)
        self.assertEqual(first_result['last_name'], first_course.last_name)
        self.assertEqual(first_result['email'], first_course.email)
        self.assertEqual(first_result['is_active'], first_course.is_active)

    def test_detail(self):
        user = models.DjangoUser.objects.order_by('last_name', 'first_name', 'username').first()
        response = self.client.get(path=reverse('core:users-detail', kwargs={'pk': user.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['id'], user.id)
        self.assertEqual(response.data['username'], user.username)
        self.assertEqual(response.data['first_name'], user.first_name)
        self.assertEqual(response.data['last_name'], user.last_name)
        self.assertEqual(response.data['email'], user.email)
        self.assertEqual(response.data['is_active'], user.is_active)
        self.assertEqual(response.data['is_staff'], user.is_staff)
        self.assertEqual(response.data['is_superuser'], user.is_superuser)

    def test_filter_username(self):
        users = models.DjangoUser.objects.order_by('id')
        username_part = users.first().username[1:-1]
        response = self.client.get(path=reverse('core:users-list'), data={'username': username_part})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_users = users.filter(username__icontains=username_part)
        actual_ids = list(expected_users.values_list('id', flat=True))
        expected_ids = list(map(lambda user: user['id'], response.data['results']))
        self.assertEqual(expected_ids, actual_ids)

    def test_create(self):
        data = {
            'username': 'user',
            'password': 'password123',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'user@example.com',
            'is_active': True,
            'is_staff': False,
            'is_superuser': False,
        }

        response = self.client.post(reverse('core:users-list'), data=data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_user = models.DjangoUser.objects.order_by('id').last()
        self.assertEqual(data['username'], created_user.username)
        self.assertTrue(created_user.check_password(data['password']))
        self.assertEqual(data['first_name'], created_user.first_name)
        self.assertEqual(data['last_name'], created_user.last_name)
        self.assertEqual(data['email'], created_user.email)
        self.assertEqual(data['is_active'], created_user.is_active)
        self.assertEqual(data['is_staff'], created_user.is_staff)
        self.assertEqual(data['is_superuser'], created_user.is_superuser)

    def test_create_not_password(self):
        data = {
            'username': 'user',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'user@example.com',
            'is_active': True,
            'is_staff': False,
            'is_superuser': False,
        }

        response = self.client.post(reverse('core:users-list'), data=data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update(self):
        data = {
            'username': 'new_user',
            'password': 'newpassword123',
            'first_name': 'new New',
            'last_name': 'new User',
            'email': 'new_user@example.com',
            'is_active': False,
            'is_staff': False,
            'is_superuser': False,
        }
        user = models.DjangoUser.objects.order_by('id').first()
        response = self.client.put(path=reverse('core:users-detail', kwargs={'pk': user.id}), data=data,
                                   content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user.refresh_from_db()
        self.assertEqual(data['username'], user.username)
        self.assertTrue(user.check_password(data['password']))
        self.assertEqual(data['first_name'], user.first_name)
        self.assertEqual(data['last_name'], user.last_name)
        self.assertEqual(data['email'], user.email)
        self.assertEqual(data['is_active'], user.is_active)
        self.assertEqual(data['is_staff'], user.is_staff)
        self.assertEqual(data['is_superuser'], user.is_superuser)

    def test_update_not_password(self):
        original_password = 'originalpassword123'
        user = models.DjangoUser.objects.create_user(
            username='original_user',
            password=original_password,
            first_name='New',
            last_name='User',
            email='user@example.com',
            is_active=True,
            is_staff=False,
            is_superuser=False
        )

        data = {
            'username': 'new_user',
            'first_name': 'new New',
            'last_name': 'new User',
            'email': 'new_user@example.com',
            'is_active': False,
            'is_staff': False,
            'is_superuser': False,
        }

        response = self.client.put(path=reverse('core:users-detail', kwargs={'pk': user.id}), data=data,
                                   content_type="application/json")
        if response.status_code != status.HTTP_200_OK:
            print("Response data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user.refresh_from_db()
        self.assertEqual(data['username'], user.username)
        self.assertTrue(user.check_password(original_password))
        self.assertEqual(data['first_name'], user.first_name)
        self.assertEqual(data['last_name'], user.last_name)
        self.assertEqual(data['email'], user.email)
        self.assertEqual(data['is_active'], user.is_active)
        self.assertEqual(data['is_staff'], user.is_staff)
        self.assertEqual(data['is_superuser'], user.is_superuser)

    def test_delete(self):
        user = models.DjangoUser.objects.order_by('id').first()

        response = self.client.delete(path=reverse('core:users-detail', kwargs={'pk': user.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(models.Student.objects.filter(id=user.id).exists())
