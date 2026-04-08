from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
def create_students():
    Student.objects.create(
        name="Олександр Іваненко",
        year_of_study=2,
        stud_id="S123456789"
    )

    Student.objects.create(
        name="Марія Петренко",
        year_of_study=3,
        stud_id="S987654321"
    )
def update_student_year(stud_id, new_year):
    try:
        student = Student.objects.get(stud_id=stud_id)
        student.year_of_study = new_year
        student.save()
        return True
    except Student.DoesNotExist:
        return False
def delete_graduated_students():
    Student.objects.filter(year_of_study=5).delete()
def get_students_sorted():
    return Student.objects.all().order_by('-year_of_study')
def index(request):
    # створення
    create_students()

    # оновлення
    update_student_year("S123456789", 3)

    # видалення
    delete_graduated_students()

    # отримання і вивід
    students = get_students_sorted()

    result = ""
    for s in students:
        result += f"{s.name} - {s.year_of_study} курс, ID: {s.stud_id}<br>"

    return HttpResponse(result)
# Create your views here.
