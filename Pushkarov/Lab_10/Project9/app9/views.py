from django.shortcuts import render
from django.db import models
from .models import Student
from .models import Course
Student.objects.get_or_create(
    Student_ID='S123456789', 
    defaults={'Name': 'Олександр Іваненко', 'Year': 2}
)
Student.objects.get_or_create(
    Student_ID='S987654321', 
    defaults={'Name': 'Марія Петренко', 'Year': 3}
)
def get_student_list():
    students = Student.objects.filter(Year=3).values('Name', 'Year')
    return list(students)
def check_student_by_id(student_id):
    exists = Student.objects.filter(Student_ID=student_id).exists()
    if exists:
        student = Student.objects.get(Student_ID=student_id)
        return f"Студент {student.Name} (Курс: {student.Year}) знайдений у базі."
    return "Студента з таким ID не знайдено."

def count_students_by_year():
    stats = Student.objects.values('Year').annotate(total=models.Count('id')).order_by('Year')
    return list(stats)

def get_students_above_year_2_raw():
    query = "SELECT id, Name, Year FROM app9_student WHERE Year > 2"
    students = Student.objects.raw(query)
    return [{"Name": s.Name, "Year": s.Year} for s in students]

def get_long_courses_dict():
    long_courses = Course.objects.filter(Duration_Hours__gt=100).values('Course_Name', 'Duration_Hours')
    
    return {c['Course_Name']: c['Duration_Hours'] for c in long_courses}