from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(default='1')
    city = models.CharField(max_length=100)
