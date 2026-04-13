from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    full_name = models.CharField(max_length=150)
    year_of_study = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    student_id = models.CharField(max_length=10, unique=True)
class Course(models.Model):
    Course_name = models.CharField(max_length=25)
    DurationHours= models.IntegerField()