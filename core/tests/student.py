from django.urls import reverse
from rest_framework import status

from core.tests.base import BaseRestTestCase
from core import factories, models
from lib.string import clean_phone_number


class Student(BaseRestTestCase):
    any_permissions = ['core.view_student', 'core.add_student', 'core.change_student', 'core.delete_student']

    def generate_data(self):
        factories.Student.create_batch(5)

    def test_list(self):
        response = self.client.get(path=reverse('core:students-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_courses = models.Student.objects.order_by('id')
        expected_ids = list(map(lambda student: student['id'], response.data['results']))
        actual_ids = list(expected_courses.values_list('id', flat=True))
        self.assertEqual(expected_ids, actual_ids)

        first_student = expected_courses.first()
        first_result = response.data['results'][0]

        self.assertEqual(first_student.id, first_result['id'])
        self.assertEqual(first_student.telegram_id, first_result['telegram_id'])
        self.assertEqual(first_student.username, first_result['username'])
        self.assertEqual(first_student.name, first_result['name'])
        self.assertEqual(first_student.phone_number, first_result['phone_number'])

    def test_create(self):
        data = {
            "telegram_id": 123467,
            "username": 'student username',
            "name": 'student name',
            "phone_number": '+7 (999) 999-99-99',
        }
        response = self.client.post(path=reverse('core:students-list'), data=data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_student = models.Student.objects.order_by('id').last()
        self.assertEqual(data['telegram_id'], created_student.telegram_id)
        self.assertEqual(data['username'], created_student.username)
        self.assertEqual(data['name'], created_student.name)
        self.assertEqual(clean_phone_number(data['phone_number']), created_student.phone_number)

    def test_update(self):
        data = {
            "telegram_id": 1234678,
            "username": 'new student username',
            "name": 'new student name',
            "phone_number": '+79999999998',
        }
        student = models.Student.objects.order_by('id').first()
        response = self.client.put(path=reverse('core:students-detail', kwargs={'pk': student.id}), data=data,
                                   content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        student.refresh_from_db()
        self.assertEqual(data['username'], student.username)
        self.assertEqual(data['name'], student.name)
        self.assertEqual(data['phone_number'], student.phone_number)

    def test_delete(self):
        student = models.Student.objects.order_by('id').first()

        response = self.client.delete(path=reverse('core:students-detail', kwargs={'pk': student.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(models.Student.objects.filter(id=student.id).exists())
