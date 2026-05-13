from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    study_year = models.IntegerField()
    student_card = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.full_name} ({self.study_year} рік)"
