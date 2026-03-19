from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    full_name = models.CharField(max_length=150)
    year_of_study = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    student_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.full_name


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    duration_hours = models.IntegerField()

    def __str__(self):
        return self.course_name