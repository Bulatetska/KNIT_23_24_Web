from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    year_of_study = models.IntegerField()
    stud_id = models.CharField(max_length=100, unique=True, default="")

class Course(models.Model):
    name = models.CharField(max_length=100)
    hours = models.IntegerField()
# Create your models here.
