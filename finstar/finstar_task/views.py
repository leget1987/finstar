from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import action
from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from jsonschema import validate, exceptions
from rest_framework import status

from finstar_task.filters import ProductFilter, ReceiptFilter
from finstar_task.serializers import *


def create_receipt(request):
    schema = {
        "type": "object",
        "properties": {
            "user": {"type": "object",
                     "properties": {"name":
                         {
                             "type": "string"
                         }
                     }
                     },
            "shop": {"type": "object",
                     "properties": {"name":
                                        {"type": "string"}
                                    }
                     },
            "time_issuance": {"type": "string"},
            "date_issuance": {"type": "string"},
            "number_receipt": {"type": "number", "minimum": 1},
            "sum_receipt": {"type": "number", "minimum": 0},
            "product": {"type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "quantity": {"type": "number", "minimum": 1},
                            "price": {"type": "number", "minimum": 1},
                        }
                        }
        }
    }

    try:
        validate(request, schema)
        user = Consumer.objects.get_or_create(name=request['user']['name'])
        shop = Shop.objects.get_or_create(name=request['shop']['name'])
        receipt_id = Receipt.objects.create(user=user[0], shop=shop[0],
                                            time_issuance=request['time_issuance'],
                                            date_issuance=request['date_issuance'],
                                            number_receipt=request['number_receipt'],
                                            sum_receipt=request['sum_receipt'])
        Product.objects.create(receipt=receipt_id, name=request['product']['name'],
                               quantity=request['product']['quantity'],
                               price=request['product']['price'])
        return Response(data='all right')
    except exceptions.ValidationError:
        return Response(data=f'Неверный формат данных, схема данных данных:{schema}',
                        status=status.HTTP_400_BAD_REQUEST)


class ReceiptView(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

    @action(detail=False)
    def sum_receipt_in_interval(self, request, *args, **kwargs):
        start_date_param = request.query_params.get('start_date', None)
        end_date_param = request.query_params.get('end_date', None)
        request_params = {'date_issuance__gte': start_date_param,
                          'date_issuance__lte': end_date_param}
        params = {}
        for key, value in request_params.items():
            if value:
                params[key] = value
        result_queryset = Receipt.objects.filter(**params)
        result = result_queryset.aggregate(total_sum=Sum('sum_receipt'))
        result['дата начала периода отчета'] = [start_date_param if start_date_param else 'не задана']
        result['дата конца периода отчета'] = [end_date_param if end_date_param else 'не задана']
        return Response(result)

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, dict):
            result = create_receipt(request.data)
        elif isinstance(request.data, list):
            for i in request.data:
                result = create_receipt(i)
                if result.status_code == status.HTTP_400_BAD_REQUEST:
                    result.data = f'Чек {i} и следующие после него не записались, неверный форма'
                    break
        else:
            return Response(data=f'Неверный формат данных')
        return result


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


class ReceiptListView(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Receipt.objects.all()
    serializer_class = ReceiptListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ReceiptFilter

    @action(detail=False)
    def sum_receipt_in_interval(self, request, *args, **kwargs):
        start_date_param = request.query_params.get('start_date', None)
        end_date_param = request.query_params.get('end_date', None)
        date = request.query_params.get('date', None)
        request_params = {'date_issuance__gte': start_date_param,
                          'date_issuance__lte': end_date_param,
                          'date_issuance': date}
        params = {}
        for key, value in request_params.items():
            if value:
                params[key] = value
        result_queryset = Receipt.objects.filter(**params)
        serializer = self.get_serializer(result_queryset, context={'request': request}, many=True)
        return Response(serializer.data)
