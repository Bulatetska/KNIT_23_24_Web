from .models import Student

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
    return Student.objects.all().order_by('-year_of_study')

"""
| python manage.py shell

Student.objects.all().delete()

from lab.views import *

create_students()

for s in Student.objects.all():
    print(s.full_name, s.year_of_study, s.student_id)

update_year("S123456789", 4)

print(delete_graduated_students())

students = get_students_sorted()
for s in Student.objects.all():
    print(s.full_name, s.year_of_study, s.student_id)

"""