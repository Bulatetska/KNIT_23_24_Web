from django.http import HttpResponse
from .models import Student, Course
from django.db.models import Count

def index(request):
    # Початкові дані
    if Student.objects.count() == 0:
        Student.objects.create(full_name="Іван Іваненко", year_of_study=3, student_id="S000000001")
        Student.objects.create(full_name="Марія Петренко", year_of_study=3, student_id="S000000002")
        Student.objects.create(full_name="Олег Сидоренко", year_of_study=2, student_id="S000000003")
        Student.objects.create(full_name="Анна Коваленко", year_of_study=1, student_id="S000000004")

    if Course.objects.count() == 0:
        Course.objects.create(course_name="Python", duration_hours=120)
        Course.objects.create(course_name="Django", duration_hours=80)
        Course.objects.create(course_name="Machine Learning", duration_hours=150)

    result = ""

    # Завдання 1 — студенти 3-го курсу (розділ 2 лекції — values())
    result += "<h2>Завдання 1 — Студенти 3-го курсу:</h2>"
    third_year = Student.objects.filter(year_of_study=3).values("full_name", "year_of_study")
    for s in third_year:
        result += f"{s['full_name']} — рік {s['year_of_study']}<br>"

    # Завдання 2 — перевірка наявності студента (розділ 5 лекції — exists())
    result += "<h2>Завдання 2 — Перевірка студента:</h2>"
    result += check_student("S000000001")
    result += "<br>"
    result += check_student("S999999999")

    # Завдання 3 — групування за роком (розділ 4 лекції — annotate)
    result += "<h2>Завдання 3 — Кількість студентів по курсах:</h2>"
    groups = Student.objects.values("year_of_study").annotate(count=Count("id")).order_by("year_of_study")
    for g in groups:
        result += f"Рік {g['year_of_study']}: {g['count']} студентів<br>"

    # Завдання 4 — SQL запит через raw() (розділ 1 лекції)
    result += "<h2>Завдання 4 — SQL запит (рік > 2):</h2>"
    students_raw = Student.objects.raw("SELECT * FROM university_student WHERE year_of_study > 2")
    for s in students_raw:
        result += f"{s.full_name} — рік {s.year_of_study}<br>"

    # Завдання 5 — курси більше 100 годин у вигляді словника (розділ 3 лекції — values())
    result += "<h2>Завдання 5 — Курси більше 100 годин:</h2>"
    long_courses = get_long_courses()
    for course in long_courses:
        result += f"{course['course_name']}: {course['duration_hours']} годин<br>"

    return HttpResponse(result)


def check_student(student_id):
    if Student.objects.filter(student_id=student_id).exists():
        student = Student.objects.get(student_id=student_id)
        return f"✅ Студент знайдений: {student.full_name}"
    else:
        return f"❌ Студента з квитком {student_id} не знайдено"


def get_long_courses():
    courses = Course.objects.filter(duration_hours__gt=100).values("course_name", "duration_hours")
    return list(courses)