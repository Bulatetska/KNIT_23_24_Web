from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    full_name = models.CharField("ПІБ студента", max_length=150)
    year_of_study = models.PositiveIntegerField(
        "Рік навчання", 
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    student_id = models.CharField("Номер студентського квитка", max_length=10, unique=True)
    
    def __str__(self):
        return self.full_name

class Course(models.Model):
    course_name = models.CharField("Назва курсу", max_length=100)
    duration_hours = models.PositiveIntegerField("Тривалість (годин)")
    
    def __str__(self):
        return self.course_name