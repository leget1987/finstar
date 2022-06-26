from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.renderers import JSONRenderer
from finstar_task.models import *
from rest_framework.decorators import action
from finstar_task.serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from finstar_task.filters import ProductFilter, ReceiptFilter

# Create your views here.


class ReceiptView(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

    @action(detail=False)
    def count_cases_by_operator(self, request, *args, **kwargs):
        start_date_param = request.query_params.get('start_date', None)
        end_date_param = request.query_params.get('end_date', None)


class ProductView(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Product.objects.all()
    serializer_class = ProductForUserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter


class ShopView(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class UserShopView(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Receipt.objects.all()
    serializer_class = UserShopViewSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ReceiptFilter
