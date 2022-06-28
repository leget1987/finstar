from django.db import models
from django.utils import timezone


# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=50, verbose_name='Магазин')

    def __str__(self):
        return f'Магазин {self.name}'


class Consumer(models.Model):
    name = models.CharField(max_length=50, verbose_name='Магазин')

    def __str__(self):
        return f'Покупатель {self.name}'


class Receipt(models.Model):
    user = models.ForeignKey(to=Consumer, on_delete=models.CASCADE)
    shop = models.ForeignKey(to=Shop, on_delete=models.CASCADE, verbose_name='Магазин', related_name='receipt')
    number_receipt = models.PositiveSmallIntegerField()
    time_issuance = models.TimeField(default=timezone.now)
    date_issuance = models.DateField(default=timezone.now)
    sum_receipt = models.FloatField()

    def __str__(self):
        return f"Чек №{self.number_receipt}"


class Product(models.Model):
    receipt = models.ForeignKey(to=Receipt, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=150)
    quantity = models.PositiveSmallIntegerField()
    price = models.FloatField()

    def total(self):
        return self.quantity * self.price

    def __str__(self):
        return self.name
