import factory
from faker import Factory

from core import models


factory_ru = Factory.create('ru_RU')


class Student(factory.django.DjangoModelFactory):
    telegram_id = factory.Sequence(lambda n: n + 10000)
    username = factory.Faker('word', locale='ru_RU')
    name = factory.Faker('word', locale='ru_RU')
    phone_number = factory.LazyFunction(lambda: factory_ru.phone_number())

    class Meta:
        model = models.Student


class Course(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: factory_ru.word())
    description = factory.Sequence(lambda n: factory_ru.word())
    is_active = factory.Faker('boolean')

    class Meta:
        model = models.Course
