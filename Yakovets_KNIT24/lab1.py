import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_test.settings')
django.setup()

from shop.models import Student 

def run_lab():
    print("--- Початок виконання завдань ---")


    s1, created1 = Student.objects.get_or_create(
        full_name="Олександр Іваненко", 
        study_year=2, 
        student_card="S123456789"
    )
    s2, created2 = Student.objects.get_or_create(
        full_name="Марія Петренко", 
        study_year=3, 
        student_card="S987654321"
    )
    print("Статус: Студенти додані/перевірені.")

    Student.objects.filter(student_card="S987654321").update(study_year=4)
    print("Статус: Рік навчання для S987654321 оновлено.")

    deleted = Student.objects.filter(study_year=5).delete()
    print(f"Статус: Видалено випускників (5 курс): {deleted[0]}")

    print("\n--- Список студентів (сортування за роком навчання) ---")
    all_students = Student.objects.all().order_by('-study_year')
    for s in all_students:
        print(f"Студент: {s.full_name} | Курс: {s.study_year} | Квиток: {s.student_card}")

if __name__ == "__main__":
    run_lab()