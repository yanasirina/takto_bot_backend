from django.urls import reverse
from rest_framework import status

from core.tests.base import BaseRestTestCase
from promo import factories, models


class PromoCode(BaseRestTestCase):
    any_permissions = ['promo.view_promocode', 'promo.add_promocode', 'promo.change_promocode', 'promo.delete_promocode']

    def generate_data(self):
        factories.PromoCode.create_batch(4)

    def test_list(self):
        response = self.client.get(path=reverse('promo:promocodes-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_courses = models.PromoCode.objects.order_by('id')
        expected_ids = list(map(lambda promocode: promocode['id'], response.data['results']))
        actual_ids = list(expected_courses.values_list('id', flat=True))
        self.assertEqual(expected_ids, actual_ids)

        first_promocode = expected_courses.first()
        first_result = response.data['results'][0]

        self.assertEqual(first_promocode.id, first_result['id'])
        self.assertEqual(first_promocode.name, first_result['name'])
        self.assertEqual(first_promocode.student.id, first_result['student'])
        self.assertEqual(first_promocode.description, first_result['description'])
        self.assertEqual(first_promocode.is_active, first_result['is_active'])

    def test_create(self):
        student = factories.Student()

        data = {
            "name": 'Promocode',
            "student": student.id,
            "description": 'Promocode description'
        }
        response = self.client.post(path=reverse('promo:promocodes-list'), data=data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_promocode = models.PromoCode.objects.order_by('id').last()
        self.assertEqual(data['name'], created_promocode.name)
        self.assertEqual(data['student'], created_promocode.student.id)
        self.assertEqual(data['description'], created_promocode.description)
        self.assertTrue(created_promocode.is_active)

    def test_update(self):
        student = factories.Student()

        data = {
            "name": 'new Promocode',
            "student": student.id,
            "description": 'new Promocode description',
            "phone_number": '+79999999998',
            "is_active": False
        }
        promocode = models.PromoCode.objects.order_by('id').first()
        response = self.client.put(path=reverse('promo:promocodes-detail', kwargs={'pk': promocode.id}), data=data,
                                   content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        promocode.refresh_from_db()
        self.assertEqual(data['name'], promocode.name)
        self.assertEqual(data['student'], promocode.student.id)
        self.assertEqual(data['description'], promocode.description)
        self.assertEqual(data['is_active'], promocode.is_active)

    def test_delete(self):
        promocode = models.PromoCode.objects.order_by('id').first()

        response = self.client.delete(path=reverse('promo:promocodes-detail', kwargs={'pk': promocode.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(models.PromoCode.objects.filter(id=promocode.id).exists())
