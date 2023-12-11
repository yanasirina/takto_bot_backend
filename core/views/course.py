from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from core import models, filters, serializers
from core.permissions import DjangoModelPermissions
from core.views.pagination import RestPagination


class CourseViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)
    queryset = models.Course.objects.all()
    pagination_class = RestPagination
    filterset_class = filters.Course
    serializer_class = serializers.Course

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.CourseShort
        return super().get_serializer_class()
