from django.db import models

class Student(models.Model): 
    full_name = models.CharField(max_length=100)
    year = models.IntegerField()
    ticket = models.CharField(max_length=20, unique=True)