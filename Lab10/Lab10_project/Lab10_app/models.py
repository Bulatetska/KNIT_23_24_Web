from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    year_of_study = models.IntegerField()

class Course(models.Model):
    name = models.CharField(max_length=100)
    hours = models.IntegerField()
# Create your models here.
