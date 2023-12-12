from django.contrib.auth import get_user_model
from django.db import models


DjangoUser = get_user_model()


class Course(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    is_active = models.BooleanField('Статус', default=False, help_text='ведется ли запись на курс')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name
