from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from core import models, filters, serializers
from core.permissions import DjangoModelPermissions
from core.views.pagination import RestPagination


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)
    queryset = models.DjangoUser.objects.all().order_by('last_name', 'first_name', 'username')
    pagination_class = RestPagination
    filterset_class = filters.User
    serializer_class = serializers.User
