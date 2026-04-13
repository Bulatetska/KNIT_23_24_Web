from .models import Student
def create_students():
    Student.objects.update_or_create(
        student_id='S123456789',
        defaults={'full_name': 'Олександр Іваненко', 'year_of_study': 2}
    )
    Student.objects.update_or_create(
        student_id='S987654321',
        defaults={'full_name': 'Марія Петренко', 'year_of_study': 3}
    )

def update_year(s_id, new_year):
    student = Student.objects.get(student_id=s_id)
    student.year_of_study = new_year
    student.save()
    return f"Курс студента {student.full_name} змінено на {new_year}."

def delete_graduated():
    deleted_count, _ = Student.objects.filter(year_of_study=5).delete()
    return deleted_count

def get_sorted_students():
    return Student.objects.all().order_by('-year_of_study')
"""from django.db.models import Count
from .models import Student, Course

def create_initial_students():
    Student.objects.update_or_create(
        student_id='S123456789',
        defaults={'full_name': 'Олександр Іваненко', 'year_of_study': 2}
    )
    Student.objects.update_or_create(
        student_id='S987654321',
        defaults={'full_name': 'Марія Петренко', 'year_of_study': 3}
    )
    return "Студенти створені."

def get_third_year_students():
    return list(Student.objects.filter(year_of_study=3).values('full_name', 'year_of_study'))

def check_student_by_id(s_id):
    student = Student.objects.filter(student_id=s_id).first()
    if student:
        return f"Студент {student.full_name} знайдений."
    return "Студента не знайдено."

def count_students_by_year():
    return list(Student.objects.values('year_of_study').annotate(total=Count('id')))

def get_students_above_year_2_raw():
    query = "SELECT id, full_name, year_of_study FROM hello_student WHERE year_of_study > 2"
    return Student.objects.raw(query)

def get_long_courses_dict():
    courses = Course.objects.filter(DurationHours__gt=100)
    return {c.Course_name: c.DurationHours for c in courses}

def update_student_year(s_id, new_year):
    updated = Student.objects.filter(student_id=s_id).update(year_of_study=new_year)
    if updated:
        return "Оновлено."
    return "Не знайдено."

def delete_graduated():
    count, _ = Student.objects.filter(year_of_study=5).delete()
    return f"Видалено випускників: {count}"

def get_students_reversed():
    return Student.objects.all().order_by('-year_of_study')"""