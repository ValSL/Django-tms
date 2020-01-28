from django.db import models


class NatureImage(models.Model):
    url = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()
    comment = models.CharField(max_length=255)
