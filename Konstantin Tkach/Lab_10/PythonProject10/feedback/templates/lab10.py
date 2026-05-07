import os
import django
from django.db.models import Count

# Налаштування Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from feedback.models import Student, Course


def run_lab_10():
    print("\n=== ЛАБОРАТОРНА РОБОТА №10: АНАЛІТИКА ===")

    # 1. Список студентів 3 курсу (тільки ПІБ та рік)
    print("\n--- 1. Студенти 3 курсу ---")
    third_year = Student.objects.filter(year_of_study=3).values('full_name', 'year_of_study')
    for s in third_year:
        print(f"Студент: {s['full_name']}, Курс: {s['year_of_study']}")

    # 2. Перевірка наявності студента за ID
    print("\n--- 2. Перевірка за ID ---")

    def check_student(s_id):
        exists = Student.objects.filter(student_id=s_id).exists()
        return f"Студент з ID {s_id} знайдений." if exists else "Студента не знайдено."

    print(check_student("S123456789"))  # Перевіряємо Олександра

    # 3. Групування та підрахунок студентів на кожному курсі
    print("\n--- 3. Кількість студентів по курсах ---")
    stats = Student.objects.values('year_of_study').annotate(total=Count('id'))
    for item in stats:
        print(f"Курс {item['year_of_study']}: {item['total']} студентів")

    # 4. SQL-запит через raw() (курс > 2)
    print("\n--- 4. SQL-запит (курс > 2) ---")
    # Використовуємо назву таблиці 'feedback_student' (зазвичай це додаток_модель)
    raw_students = Student.objects.raw('SELECT * FROM feedback_student WHERE year_of_study > 2')
    for s in raw_students:
        print(f"Знайдено SQL: {s.full_name} ({s.year_of_study} курс)")

    # 5. Пошук курсів > 100 годин у вигляді словника
    print("\n--- 5. Курси > 100 годин (словник) ---")
    long_courses = Course.objects.filter(duration_hours__gt=100).values('course_name', 'duration_hours')
    courses_dict = {item['course_name']: item['duration_hours'] for item in long_courses}
    print(courses_dict)


if __name__ == "__main__":
    run_lab_10()