import sys

from rest_framework.pagination import PageNumberPagination


class RestPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'per_page'

    def get_page_size(self, request):
        if request.query_params.get(self.page_size_query_param) == 'all':
            return sys.maxsize
        else:
            return super().get_page_size(request)
