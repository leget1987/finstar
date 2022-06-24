import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=50, verbose_name='Магазин')

    def __str__(self):
        return f'Магазин {self.name}'


class Receipt(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    shop = models.ForeignKey(to=Shop, on_delete=models.CASCADE, verbose_name='Магазин')
    number_receipt = models.PositiveSmallIntegerField()
    time_issuance = models.TimeField(default=datetime.time)
    sum_receipt = models.FloatField()

    def __str__(self):
        return f"Чек №{self.number_receipt}"


class Product(models.Model):
    receipt = models.ForeignKey(to=Receipt, on_delete=models.CASCADE, related_name='product')
    name = models.CharField(max_length=150)
    quantity = models.PositiveSmallIntegerField()
    price = models.FloatField()

    def total(self):
        return self.quantity * self.price

    def __str__(self):
        return self.name
