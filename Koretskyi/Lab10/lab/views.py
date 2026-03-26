from .models import Student, Course
from django.db.models import Count

def create_students():
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
def create_courses():
    Course.objects.create(
        course_name="Програмування",
        duration_hours=120,
    )
def update_year(student_id, new_year):
    try:
        student = Student.objects.get(student_id=student_id)
        student.year_of_study = new_year
        student.save()
        return "Оновлено"
    except Student.DoesNotExist:
        return "Студента не знайдено"

def delete_graduated_students():
    deleted_count, _ = Student.objects.filter(year_of_study=5).delete()
    return f"Видалено {deleted_count} студентів"

def get_students_sorted():
    students = Student.objects.all().order_by('-year_of_study')
    for s in students:
        print(s.full_name, s.year_of_study)

def get_students_by_3_year():
    list = Student.objects.filter(year_of_study=3).values("full_name","year_of_study")
    print(f"{list}")

def student_exists(student_id):
    exists = Student.objects.filter(student_id=student_id).exists()
    if exists:
        return "Студент існує"
    else:
        return "Студента не знайдено"

def group_students_by_year():
    qs = Student.objects.values('year_of_study').annotate(count=Count('id'))
    return list(qs)

def get_students_raw():
    query = \
        "SELECT * FROM lab_student WHERE year_of_study > 2"
    return Student.objects.raw(query)

def get_long_courses():
    courses = Course.objects.filter(duration_hours__gt=100)
    return list(courses.values('course_name', 'duration_hours'))

"""
| python manage.py shell

Student.objects.all().delete()

Course.objects.all().delete()

from lab.views import *

create_students()

create_courses()

for s in Student.objects.all():
    print(s.full_name, s.year_of_study, s.student_id)

update_year("S123456789", 4)

print(delete_graduated_students())

get_students_sorted()

get_students_by_3_year()

student_exists("S123456789")

group_students_by_year()

for s in get_students_raw():
    print(s.full_name, s.year_of_study)

get_long_courses()

"""