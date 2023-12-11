import django_filters

from core import models


class User(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='username', lookup_expr='icontains')
    last_name = django_filters.CharFilter(field_name='last_name', lookup_expr='icontains')
    is_active = django_filters.BooleanFilter(method='filter_is_active')

    class Meta:
        model = models.DjangoUser
        fields = ['username', 'last_name', 'is_active']

    def filter_is_active(self, qs, name, value):
        return qs.filter(is_active=value)


class Student(django_filters.FilterSet):
    telegram_id = django_filters.CharFilter(field_name='telegram_id', lookup_expr='exact')

    class Meta:
        model = models.Student
        fields = ['telegram_id']
