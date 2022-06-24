from django_filters import rest_framework as filters
from finstar_task.models import *


class ProductFilter(filters.FilterSet):

    class Meta:
        model = Product
        fields = ('id', 'receipt__user__id')