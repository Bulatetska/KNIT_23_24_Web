import os
import django

# Налаштовуємо оточення Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from feedback.models import Student

def run_lab_9():
    # 1. Створення записів
    print("--- Крок 1: Створення записів ---")
    s1, created1 = Student.objects.get_or_create(
        student_id="S123456789",
        defaults={'full_name': "Олександр Іваненко", 'year_of_study': 2}
    )
    s2, created2 = Student.objects.get_or_create(
        student_id="S987654321",
        defaults={'full_name': "Марія Петренко", 'year_of_study': 3}
    )
    print(f"Додано/Перевірено: {s1.full_name}, {s2.full_name}")

    # 2. Оновлення року навчання за student_id
    print("\n--- Крок 2: Оновлення року навчання ---")
    Student.objects.filter(student_id="S123456789").update(year_of_study=3)
    print("Олександр Іваненко тепер на 3 курсі.")

    # 3. Видалення випускників (курс = 5)
    print("\n--- Крок 3: Видалення студентів 5 курсу ---")
    deleted = Student.objects.filter(year_of_study=5).delete()
    print(f"Видалено записів: {deleted[0]}")

    # 4. Сортування (зворотний порядок за роком навчання)
    print("\n--- Крок 4: Всі студенти (сортування за спаданням курсу) ---")
    students = Student.objects.all().order_by('-year_of_study')
    for s in students:
        print(f"Курс {s.year_of_study}: {s.full_name} (ID: {s.student_id})")

if __name__ == "__main__":
    run_lab_9()