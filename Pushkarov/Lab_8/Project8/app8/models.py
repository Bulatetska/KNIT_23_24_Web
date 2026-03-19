from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator

class Student(models.Model):
 Full_Name = models.CharField(max_length=150)
 Year_of_Study = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
 Student_ID = models.CharField(max_length=10, validators=[MinLengthValidator(10)], unique=True)
 def __str__(self):
  return self.Full_Name

class Course(models.Model):
 Course_Name = models.CharField(max_length=100)
 Duration_Hours = models.IntegerField(validators=[MinValueValidator(1)])
 def __str__(self):
  return self.Course_Name
