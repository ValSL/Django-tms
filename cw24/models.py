from django.db import models


class AnimalImage(models.Model):
    url = models.CharField(max_length=255)
    species = models.CharField(max_length=20)
    created = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=100)
