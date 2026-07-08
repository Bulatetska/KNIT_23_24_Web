from students_app.models import Student, Course
from django.db.models import Count

# Створення даних
Student.objects.get_or_create(full_name="Ковалюк Денис", year_of_study=3, student_id="ВНУ-001")
Student.objects.get_or_create(full_name="Шевченко Тарас", year_of_study=1, student_id="ВНУ-002")
Student.objects.get_or_create(full_name="Франко Іван", year_of_study=4, student_id="ВНУ-003")

Course.objects.get_or_create(name="Програмування на C++", duration_hours=120)
Course.objects.get_or_create(name="Основи Python", duration_hours=80)
Course.objects.get_or_create(name="Кібербезпека", duration_hours=150)

print("\n--- 1. Студенти 3 курсу ---")
print(list(Student.objects.filter(year_of_study=3).values('full_name', 'year_of_study')))

print("\n--- 2. Перевірка наявності студента ---")
print("ВНУ-001 знайдено:", Student.objects.filter(student_id="ВНУ-001").exists())
print("ВНУ-999 знайдено:", Student.objects.filter(student_id="ВНУ-999").exists())

print("\n--- 3. Кількість студентів по курсах ---")
for group in Student.objects.values('year_of_study').annotate(count=Count('id')).order_by('year_of_study'):
    print(f"Курс {group['year_of_study']}: {group['count']} студент(ів)")

print("\n--- 4. Студенти старше 2 курсу (через SQL raw) ---")
for student in Student.objects.raw("SELECT * FROM students_app_student WHERE year_of_study > 2"):
    print(f"- {student.full_name} ({student.year_of_study} курс)")

print("\n--- 5. Курси > 100 годин ---")
print(list(Course.objects.filter(duration_hours__gt=100).values('name', 'duration_hours')))
