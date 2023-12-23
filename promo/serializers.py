from rest_framework import serializers

from promo import models


class PromoCode(serializers.ModelSerializer):
    class Meta:
        model = models.PromoCode
        fields = ['id', 'name', 'student', 'description', 'is_active']
