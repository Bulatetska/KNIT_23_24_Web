from django.shortcuts import render
from .models import Student

student_1 = Student.objects.create(full_name="Олександр Іваненко", year_of_study="2", student_id="S123456789")
student_2 = Student.objects.create(full_name="Марія Петренко", year_of_study="3", student_id="S987654321")

def update_student(student_id, year_of_study):
    student = Student.objects.filter(student_id=student_id).update(year_of_study=year_of_study)

def delete_student():
    Student.objects.filter(year_of_study="5").delete()

def all_students():
    return Student.objects.order_by('-year_of_study')