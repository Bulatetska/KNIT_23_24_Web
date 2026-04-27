from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    ticket = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} | {self.year} курс | {self.ticket}"