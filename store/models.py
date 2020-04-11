from django.db import models
from datetime import datetime

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=100)
    shop_key = models.CharField(primary_key=True, max_length=6)
    slug = models.CharField(max_length=200, default=1)

    class Meta:
        verbose_name_plural = "Shops"

    def __str__(self):
        return self.name

class Item(models.Model):

    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    unit = models.CharField(max_length=10)
    date = models.DateTimeField("Added_Date", default = datetime.now())
    item_key = models.ForeignKey(Shop, on_delete = models.CASCADE)
    slug = models.CharField(max_length=200, default=1)

    class Meta:
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name
