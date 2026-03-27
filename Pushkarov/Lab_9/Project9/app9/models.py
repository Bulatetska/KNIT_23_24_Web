from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    Name = models.CharField(max_length=100)
    Year = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    Student_ID = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.Name

