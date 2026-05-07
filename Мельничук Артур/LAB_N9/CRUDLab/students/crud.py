from .models import Student

def create_students():
    if Student.objects.count() == 0:
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
        Student.objects.create(
            full_name="Микола Гриноренко",
            year_of_study=5,
            student_id="S000000005"
        )
# Завдання 2 — Оновлення року навчання (розділ 1 лекції — save())
def update_year(student_id, new_year):
    student = Student.objects.get(student_id=student_id)
    student.year_of_study = new_year
    student.save(update_fields=["year_of_study"])
    print(f"Оновлено: {student.full_name} → рік {new_year}")

# Завдання 3 — Видалення студентів 5-го року (розділ 1 лекції — filter + delete)
def delete_graduated():
    graduated = Student.objects.filter(year_of_study=5)
    count = graduated.count()
    graduated.delete()
    print(f"Видалено {count} студентів")

# Завдання 4 — Сортування за роком у зворотньому порядку (розділ 3 лекції — order_by з мінусом)
def get_students_sorted():
    students = Student.objects.order_by("-year_of_study")
    for student in students:
        print(f"{student.full_name} — рік {student.year_of_study}")
    return students