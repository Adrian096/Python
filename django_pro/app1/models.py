from django.db import models

# Create your models here.
class Student(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    nr_albumu = models.IntegerField()
