import factory
from faker import Factory

from core import models


factory_ru = Factory.create('ru_RU')


class Course(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: factory_ru.word())
    description = factory.Sequence(lambda n: factory_ru.word())
    is_active = factory.Faker('boolean')

    class Meta:
        model = models.Course
