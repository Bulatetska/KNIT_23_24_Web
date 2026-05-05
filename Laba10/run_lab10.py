import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import Student, Course
from django.db.models import Count

def run():
    print("--- Завдання 1: 3-й курс ---")
    res1 = Student.objects.filter(year=3).values('full_name', 'year')
    for s in res1: print(s)

    print("\n--- Завдання 2: Перевірка квитка ---")
    def check_student(t):
        return "Знайдено" if Student.objects.filter(ticket_number=t).exists() else "Не знайдено"
    print(f"Квиток AB12345: {check_student('AB12345')}")

    print("\n--- Завдання 3: Групування ---")
    res3 = Student.objects.values('year').annotate(total=Count('id'))
    for item in res3: print(f"Курс {item['year']}: {item['total']} студентів")

    print("\n--- Завдання 4: Raw SQL ---")
    res4 = Student.objects.raw("SELECT * FROM myapp_student WHERE year > %s", [2])
    for s in res4: print(f"{s.full_name} (Курс: {s.year})")

    print("\n--- Завдання 5: Курси > 100 годин ---")
    res5 = list(Course.objects.filter(duration_hours__gt=100).values('title', 'duration_hours'))
    print(res5)

if __name__ == "__main__":
    run()