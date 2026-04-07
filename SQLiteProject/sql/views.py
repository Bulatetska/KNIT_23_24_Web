from django.shortcuts import render
from .models import Student
from .models import Course

def create_students():
    Student.objects.get_or_create(
        student_id="S123456789",
        defaults={"full_name": "Олександр Іваненко", "year_of_study": "2"}
    )
    Student.objects.get_or_create(
        student_id="S987654321",
        defaults={"full_name": "Марія Петренко", "year_of_study": "3"}
    )
    Student.objects.get_or_create(
        student_id="S555666777",
        defaults={"full_name": "Дмитро Коваленко", "year_of_study": "1"}
    )
    Student.objects.get_or_create(
        student_id="S111222333",
        defaults={"full_name": "Олена Сидоренко", "year_of_study": "5"}
    )
    Student.objects.get_or_create(
        student_id="S444555666",
        defaults={"full_name": "Андрій Бондар", "year_of_study": "4"}
    )

    Course.objects.get_or_create(
        course_name="Вища математика",
        defaults={"duration_hours": 120}
    )
    Course.objects.get_or_create(
        course_name="Основи програмування",
        defaults={"duration_hours": 150}
    )
    Course.objects.get_or_create(
        course_name="Бази даних",
        defaults={"duration_hours": 90}
    )

def update_student(student_id, year_of_study):
    student = Student.objects.filter(student_id=student_id).update(year_of_study=year_of_study)

def delete_student():
    Student.objects.filter(year_of_study="5").delete()

def all_students():
    return Student.objects.order_by('-year_of_study')

def get_students():
    students = Student.objects.filter(year_of_study="3")

    for student in students:
        print(student.full_name, student.year_of_study)

def is_student(student_id):
    if Student.objects.filter(student_id=student_id).exists():
        print("Студент за цим ID наявний у базі даних")
    else:
        print("Студент за цим ID відсутній у базі даних")

def students_by_year():
    for i in range(1, 6):
        students = Student.objects.filter(year_of_study=str(i))
        print(f"Рік навчання - {i}")
        for student in students:
            print(student)

def raw_function():
    students = Student.objects.raw('SELECT * FROM sql_student WHERE year_of_study > 2')
    for student in students:
        print(student)

def course_dictionary():
    courses = Course.objects.all()
    return dict(zip(courses.course_name, courses.duration_hours))