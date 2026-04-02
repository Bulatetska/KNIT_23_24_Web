from .models import Student


def create_students():
    Student.objects.create(name="Олександр Іваненко", year=2, student_id="S123456789")
    Student.objects.create(name="Марія Петренко", year=3, student_id="S987654321")


from django.shortcuts import render

# Create your views here.
