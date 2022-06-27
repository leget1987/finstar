from django_filters import rest_framework as filters
from finstar_task.models import *


class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = ('id', 'receipt__user__id', 'receipt__shop__id',)


class ReceiptFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name="date_issuance", lookup_expr='gte')
    end_date = filters.DateFilter(field_name="date_issuance", lookup_expr='lte')
    date = filters.DateFilter(field_name="date_issuance", lookup_expr='exact')

    class Meta:
        model = Receipt
        fields = ('id', 'user', 'shop__id', 'start_date', 'end_date', 'date')
