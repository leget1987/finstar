from django.contrib import admin
from .models import *
# Register your models here.


class ShopView(admin.ModelAdmin):
    list_display = ('name',)


class ReceiptView(admin.ModelAdmin):
    list_display = ('user', 'shop', 'number_receipt', 'time_issuance', 'sum_receipt')


class ProductView(admin.ModelAdmin):
    list_display = ('receipt', 'name', 'quantity', 'price', 'total')


admin.site.register(Shop, ShopView)
admin.site.register(Receipt, ReceiptView)
admin.site.register(Product, ProductView)
