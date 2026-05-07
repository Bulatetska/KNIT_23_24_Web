from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=150)
    year_of_study = models.IntegerField()
    student_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.full_name