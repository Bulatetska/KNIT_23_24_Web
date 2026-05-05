import os
import django

# Настройка окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import Student, Course

def seed():
    # Очистка старых данных, чтобы не было дублей при повторном запуске
    Student.objects.all().delete()
    Course.objects.all().delete()

    # 1. Создание студентов (используем ticket_number)
    Student.objects.create(full_name="Іван Іванов", year=3, ticket_number="AB12345")
    Student.objects.create(full_name="Марія Петренко", year=3, ticket_number="CD67890")
    Student.objects.create(full_name="Олег Сидорчук", year=1, ticket_number="EF11223")

    # 2. Создание курсов
    Course.objects.create(title="Python Pro", duration_hours=120)
    Course.objects.create(title="Основи БД", duration_hours=40)
    Course.objects.create(title="Django Advanced", duration_hours=150)

    print("Дані успішно додані до бази!")

if __name__ == "__main__":
    seed()