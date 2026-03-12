from django.shortcuts import render
from .models import Student, Course

Student.objects.create(full_name='Петро Порошенко', year_of_study=2, student_id=101)
Course.objects.create(course_name="Комп'ютерні науки", duration_hours=2, student_id=101)

# Create your views here.
