from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    group = models.ForeignKey('Group', null=True, on_delete=models.SET_NULL, related_name='students')

    def __str__(self):
        return self.firstname


class Diary(models.Model):
    avg_mark = models.IntegerField()
    student = models.OneToOneField('Student', null=True, on_delete=models.SET_NULL, related_name='diary')


class Book(models.Model):
    name = models.CharField(max_length=100)
    pages = models.IntegerField()
    students = models.ManyToManyField('Student', related_name='books')
