import django_filters

from promo import models


class PromoCode(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    student_name = django_filters.CharFilter(field_name='student__name', lookup_expr='icontains')
    student_phone_number = django_filters.CharFilter(field_name='student__phone_number', lookup_expr='icontains')

    class Meta:
        model = models.PromoCode
        fields = ['name', 'is_active', 'student__name', 'student__phone_number']
