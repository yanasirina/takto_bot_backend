from rest_framework import serializers

from core import models
from lib.string import clean_phone_number


class User(serializers.ModelSerializer):
    class Meta:
        model = models.DjangoUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_active']


class UserDetails(serializers.ModelSerializer):
    class Meta:
        model = models.DjangoUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser']


class UserCreateUpdate(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance:
            self.fields['password'].required = True
            self.fields['password'].allow_blank = False
        else:
            self.fields['password'].required = False
            self.fields['password'].allow_blank = True

    class Meta:
        model = models.DjangoUser
        fields = ['password', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser']

    def save(self, **kwargs):
        password = self.validated_data.pop('password', None)
        instance = super().save(**kwargs)

        if password:
            instance.set_password(password)
            instance.save()

        return instance


class Student(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id', 'telegram_id', 'username', 'name', 'phone_number']

    @staticmethod
    def validate_phone_number(value):
        clean_value = clean_phone_number(value)
        return clean_value


class CourseShort(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'name', 'is_active']


class Course(CourseShort):
    class Meta:
        model = models.Course
        fields = ['id', 'name', 'description', 'is_active']
