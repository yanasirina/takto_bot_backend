from django.urls import reverse
from rest_framework import status

from core.tests.base import BaseRestTestCase
from core import factories, models


class Course(BaseRestTestCase):
    any_permissions = ['core.view_course', 'core.add_course', 'core.change_course', 'core.delete_course']

    def generate_data(self):
        factories.Course.create_batch(4)

    def test_list(self):
        response = self.client.get(path=reverse('core:courses-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_courses = models.Course.objects.order_by('id')
        expected_ids = list(map(lambda course: course['id'], response.data['results']))
        actual_ids = list(expected_courses.values_list('id', flat=True))
        self.assertEqual(expected_ids, actual_ids)

        first_course = expected_courses.first()
        first_result = response.data['results'][0]
        self.assertEqual(first_course.id, first_result['id'])
        self.assertEqual(first_course.name, first_result['name'])
        self.assertEqual(first_course.is_active, first_result['is_active'])

    def test_filter_is_active(self):
        active_courses = models.Course.objects.filter(is_active=True).order_by('id')
        not_active_courses = models.Course.objects.filter(is_active=False).order_by('id')

        response = self.client.get(path=reverse('core:courses-list'), data={'is_active': True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_ids = list(active_courses.values_list('id', flat=True))
        actual_ids = list(map(lambda course: course['id'], response.data['results']))
        self.assertEqual(expected_ids, actual_ids)

        response = self.client.get(path=reverse('core:courses-list'), data={'is_active': False})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_ids = list(not_active_courses.values_list('id', flat=True))
        actual_ids = list(map(lambda course: course['id'], response.data['results']))
        self.assertEqual(expected_ids, actual_ids)

    def test_filter_name(self):
        courses = models.Course.objects.order_by('id')
        name_part = courses.first().name[1:-1]
        response = self.client.get(path=reverse('core:courses-list'), data={'name': name_part})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_courses = courses.filter(name__icontains=name_part)
        actual_ids = list(expected_courses.values_list('id', flat=True))
        expected_ids = list(map(lambda course: course['id'], response.data['results']))
        self.assertEqual(expected_ids, actual_ids)

    def test_detail(self):
        course = models.Course.objects.order_by('id').first()
        response = self.client.get(path=reverse('core:courses-detail', kwargs={'pk': course.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['id'], course.id)
        self.assertEqual(response.data['name'], course.name)
        self.assertEqual(response.data['description'], course.description)
        self.assertEqual(response.data['is_active'], course.is_active)

    def test_create(self):
        data = {
            "name": 'course name',
            "description": 'course name',
            "is_active": True,
        }
        response = self.client.post(path=reverse('core:courses-list'), data=data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_course = models.Course.objects.order_by('id').last()
        self.assertEqual(data['name'], created_course.name)
        self.assertEqual(data['description'], created_course.description)
        self.assertEqual(data['is_active'], created_course.is_active)

    def test_update(self):
        data = {
            "name": 'new course name',
            "description": 'new course name',
            "is_active": True,
        }
        course = models.Course.objects.order_by('id').first()
        response = self.client.put(path=reverse('core:courses-detail', kwargs={'pk': course.id}), data=data,
                                   content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        course.refresh_from_db()
        self.assertEqual(data['name'], course.name)
        self.assertEqual(data['description'], course.description)
        self.assertEqual(data['is_active'], course.is_active)

    def test_delete(self):
        course = models.Course.objects.order_by('id').first()

        response = self.client.delete(path=reverse('core:courses-detail', kwargs={'pk': course.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(models.Student.objects.filter(id=course.id).exists())

