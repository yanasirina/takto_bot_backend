import django_filters

from core import models


class User(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='username', lookup_expr='icontains')
    last_name = django_filters.CharFilter(field_name='last_name', lookup_expr='icontains')

    class Meta:
        model = models.DjangoUser
        fields = ['username', 'last_name', 'is_active']


class Course(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = models.Course
        fields = ['name', 'is_active']


class Student(django_filters.FilterSet):
    class Meta:
        model = models.Student
        fields = ['telegram_id']
