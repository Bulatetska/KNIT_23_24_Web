from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Student(models.Model):
    full_name = models.CharField(max_length=150)
    year_of_study = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    student_id = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return f"[{self.student_id}, {self.full_name}, {self.year_of_study}]"

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    duration_hours = models.IntegerField(validators=[])

    def __str__(self):
        return f"[{self.course_name}, {self.duration_hours}]"