from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from core import models, filters, serializers
from core.permissions import DjangoModelPermissions
from core.views.pagination import RestPagination


class StudentViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)
    queryset = models.Student.objects.order_by('id')
    pagination_class = RestPagination
    filterset_class = filters.Student
    serializer_class = serializers.Student
