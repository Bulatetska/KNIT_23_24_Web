from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ПІБ")
    year_of_study = models.IntegerField(verbose_name="Курс")
    student_id = models.CharField(max_length=50, unique=True, verbose_name="Номер студентського")

    def __str__(self):
        return self.full_name

class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва курсу")
    duration_hours = models.IntegerField(verbose_name="Тривалість (годин)")

    def __str__(self):
        return self.name
