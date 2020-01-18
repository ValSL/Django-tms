from django.db import models


class Customer(models.Model):
    firstname = models.CharField(max_length=255, default=None)
    lastname = models.CharField(max_length=255, default=None)
    age = models.IntegerField()
    profession = models.CharField(max_length=255, default=None)

    def __str__(self):
        return f'id - {self.id} | name - {self.firstname}'
