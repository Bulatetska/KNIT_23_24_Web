from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student

def create_students():
    Student.objects.get_or_create(
        name="Олександр Іваненко",
        year_of_study=2,
        stud_id="S123456789"
    )

    Student.objects.get_or_create(
        name="Марія Петренко",
        year_of_study=3,
        stud_id="S987654321"
    )

    Student.objects.get_or_create(
        name="Петро Іваненко",
        year_of_study=5,
        stud_id="S000000000"
    )
  
def delete_students(request):
    Student.objects.filter(year_of_study=5).delete()
    students = Student.objects.all()
    return render(request, "index.html", {"students": students})

def sort_students(request):
    students = Student.objects.all().order_by('-year_of_study')
    return render(request, "index.html", {"students": students})


def index(request):
    create_students()
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})