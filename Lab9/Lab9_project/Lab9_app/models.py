from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    year_of_study = models.IntegerField()
    stud_id = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return f"{self.name} ({self.stud_id})"

# Create your models here.
