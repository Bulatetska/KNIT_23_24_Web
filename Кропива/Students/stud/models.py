from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    student_id = models.CharField(max_length=20, unique=True)


from django.db import models

# Create your models here.
