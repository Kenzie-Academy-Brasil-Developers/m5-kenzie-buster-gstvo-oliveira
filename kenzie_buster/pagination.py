from rest_framework.pagination import LimitOffsetPagination

class CustomLimitOffSet(LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = None