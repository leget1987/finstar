from rest_framework import serializers
from finstar_task.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username',)


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


