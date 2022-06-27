from rest_framework import serializers
from finstar_task.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = ('id', 'name',)


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name',)


class ReceiptSerializer(serializers.ModelSerializer):
    shop = ShopSerializer()
    user = UserSerializer()

    class Meta:
        model = Receipt
        fields = (
            'user',
            'shop',
            'number_receipt',
            'time_issuance',
            'sum_receipt',
            'date_issuance'
        )


class ProductSerializer(serializers.ModelSerializer):
    receipt = ReceiptSerializer()

    class Meta:
        model = Product
        fields = (
            'name',
            'quantity',
            'price',
            'receipt',
            'total'
        )


class UserShopViewSerializer(serializers.ModelSerializer):
    shop = ShopSerializer()

    class Meta:
        model = Receipt
        fields = (
            'shop',
        )


class ProductForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
        )


class ReceiptListSerializer(serializers.ModelSerializer):
    products = ProductForUserSerializer(many=True, read_only=True)

    class Meta:
        model = Receipt
        fields = (
            'number_receipt',
            'products'
        )
