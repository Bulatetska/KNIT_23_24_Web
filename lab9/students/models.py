from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=150, verbose_name="ПІБ")
    year = models.IntegerField(verbose_name="Рік навчання")
    student_id = models.CharField(max_length=20, unique=True, verbose_name="Студентський квиток")

    def __str__(self):
        return f"{self.name} - {self.student_id}"
