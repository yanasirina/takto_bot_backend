from rest_framework import serializers

from core import models


class User(serializers.ModelSerializer):
    class Meta:
        model = models.DjangoUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_active']


class CourseShort(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'name', 'is_active']


class Course(CourseShort):
    class Meta:
        model = models.Course
        fields = ['id', 'name', 'description', 'is_active']
