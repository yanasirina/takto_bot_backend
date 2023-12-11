from django.contrib.auth import get_user_model
from django.db import models


DjangoUser = get_user_model()


class Student(models.Model):
    telegram_id = models.BigIntegerField('User_id', unique=True)
    username = models.CharField('User_name', max_length=255, blank=True, null=True)
    name = models.CharField('Имя', max_length=255)
    phone_number = models.CharField('Номер телефона', max_length=255)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.phone_number:
            self.phone_number = self.phone_number.replace(' ', '').replace('(', '').replace(')', '').replace('-', '')
        super().save(*args, **kwargs)
