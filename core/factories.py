import factory
from faker import Factory

from core import models


factory_ru = Factory.create('ru_RU')


class Course(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: factory_ru.word())
    description = factory.Sequence(lambda n: factory_ru.word())
    is_active = bool(factory.Sequence(lambda n: factory_ru.random_int(min=0, max=2)))

    class Meta:
        model = models.Course
