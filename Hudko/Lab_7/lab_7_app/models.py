from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="ПІБ студента")
    
    year_of_study = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Рік навчання"
    )
    
    student_id = models.CharField(
        max_length=10, 
        unique=True, 
        verbose_name="Номер студентського квитка"
    )

    def __str__(self):
        return self.full_name

class Course(models.Model):
    course_name = models.CharField(max_length=200, verbose_name="Назва курсу")
    duration_hours = models.PositiveIntegerField(verbose_name="Тривалість (години)")

    def __str__(self):
        return self.course_name