from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator
from django.db import models


class Student(models.Model):
    full_name = models.CharField(max_length=150)
    year_of_study = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    student_id = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(10)])

    def __str__(self):
        return f"{self.full_name} ({self.student_id})"


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    duration_hours = models.PositiveIntegerField()

    def __str__(self):
        return self.course_name
