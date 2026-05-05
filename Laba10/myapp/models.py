from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=255)
    year = models.IntegerField()
    ticket_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.full_name

class Course(models.Model):
    title = models.CharField(max_length=255)
    duration_hours = models.IntegerField()

    def __str__(self):
        return self.title