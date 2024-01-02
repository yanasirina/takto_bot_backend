from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from core import models, filters, serializers
from core.permissions import DjangoModelPermissions
from core.views.pagination import RestPagination


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)
    queryset = models.DjangoUser.objects.all().order_by('last_name', 'first_name', 'username')
    pagination_class = RestPagination
    filterset_class = filters.User
    serializer_class = serializers.User

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.User
        elif self.action == 'retrieve':
            return serializers.UserDetails
        elif self.action in ['create', 'update', 'partial_update']:
            return serializers.UserCreateUpdate
        return super().get_serializer_class()
