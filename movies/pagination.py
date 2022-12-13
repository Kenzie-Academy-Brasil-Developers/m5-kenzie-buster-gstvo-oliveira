from rest_framework.pagination import PageNumberPagination


class CustomPageNumber(PageNumberPagination):
    page_size = 2