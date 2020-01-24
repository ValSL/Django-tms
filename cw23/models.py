from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    count = models.IntegerField()
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.name
