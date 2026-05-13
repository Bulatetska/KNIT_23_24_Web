from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=100) 
    year_of_study = models.IntegerField()         
    student_id_card = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.full_name} ({self.student_id_card})"