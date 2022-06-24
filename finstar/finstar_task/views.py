from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.renderers import JSONRenderer
from finstar_task.models import *
from finstar_task.serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from finstar_task.filters import ProductFilter

# Create your views here.


class ReceiptView(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer


class ProductView(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter


class ShopView(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer