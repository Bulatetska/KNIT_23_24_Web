from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
from .models import Student


def create_students(request):
    Student.objects.create(
        full_name="Олександр Іваненко",
        year_of_study=2,
        student_id="S123456789"
    )

    Student.objects.create(
        full_name="Марія Петренко",
        year_of_study=3,
        student_id="S987654321"
    )

    return HttpResponse("Студенти створені")
from django.http import HttpResponse
from .models import Student


def update_student(request):
    student = Student.objects.get(student_id="S123456789")
    student.year_of_study = 4
    student.save()

    return HttpResponse("Рік навчання оновлено")
def delete_graduates(request):
    Student.objects.filter(year_of_study=5).delete()

    return HttpResponse("Випускники видалені")
def list_students(request):
    students = Student.objects.all().order_by('-year_of_study')

    result = ""
    for s in students:
        result += f"{s.full_name} - {s.year_of_study} курс<br>"

    return HttpResponse(result)
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_students),
    path('update/', views.update_student),
    path('delete/', views.delete_graduates),
    path('list/', views.list_students),
]