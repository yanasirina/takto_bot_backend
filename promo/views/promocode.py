from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from promo import models, filters, serializers
from core.permissions import DjangoModelPermissions
from core.views.pagination import RestPagination


class PromoCodeViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)
    queryset = models.PromoCode.objects.order_by('id')
    pagination_class = RestPagination
    filterset_class = filters.PromoCode
    serializer_class = serializers.PromoCode
