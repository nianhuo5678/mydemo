from rest_framework import viewsets
from django.core.cache import cache
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from django.utils.encoding import force_text
from models import Student
from serializers import StudentSerializer
from rest_framework_extensions.key_constructor.bits import (
    KeyBitBase,
    RetrieveSqlQueryKeyBit,
    ListSqlQueryKeyBit,
    PaginationKeyBit
)
import datetime
from rest_framework_extensions.key_constructor.constructors import DefaultKeyConstructor


class UpdatedAtKeyBit(KeyBitBase):
    def get_data(self, **kwargs):
        key = 'api_updated_at_timestamp'
        value = cache.get(key, None)
        if not value:
            value = datetime.datetime.utcnow()
            cache.set(key, value=value)
        return force_text(value)


class CustomObjectKeyConstructor(DefaultKeyConstructor):
    retrieve_sql = RetrieveSqlQueryKeyBit()
    updated_at = UpdatedAtKeyBit()


class CustomListKeyConstructor(DefaultKeyConstructor):
    list_sql = ListSqlQueryKeyBit()
    pagination = PaginationKeyBit()
    updated_at = UpdatedAtKeyBit()


class StudentViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    object_cache_key_func = CustomObjectKeyConstructor()
    list_cache_key_func = CustomListKeyConstructor()



