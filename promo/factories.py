import factory
from faker import Factory

from promo import models
from core.factories import Student

factory_ru = Factory.create('ru_RU')


class PromoCode(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: factory_ru.word())
    student = factory.SubFactory(Student)
    description = factory.Sequence(lambda n: factory_ru.word())
    is_active = factory.Faker('boolean')

    class Meta:
        model = models.PromoCode
