from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=255)
    year = models.IntegerField()
    student_card = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.full_name} ({self.year} курс)"