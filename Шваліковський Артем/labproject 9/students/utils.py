from .models import Student


# 1. Створення студентів
from .models import Student


# 1. Створення студентів
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

    Student.objects.create(
        full_name="Артем Олександрович",
        year_of_study=2,
        student_id="S111111111"
    )

    Student.objects.create(
        full_name="Анна Петрівна",
        year_of_study=3,
        student_id="S222222222"
    )

    Student.objects.create(
        full_name="Дмитро Сергійович",
        year_of_study=2,
        student_id="S234567891"
    )

    Student.objects.create(
        full_name="Петро Павлович",
        year_of_study=5,
        student_id="S555555555"
    )

    print("Студентів створено!")


# 2. Оновлення року навчання
def update_student_year(student_id, new_year):
    try:
        student = Student.objects.get(student_id=student_id)

        student.year_of_study = new_year
        student.save()

        print(f"Оновлено рік навчання для {student.full_name}")

    except Student.DoesNotExist:
        print("Студента не знайдено")


# 3. Видалення студентів 5 курсу
def delete_graduated_students():
    deleted_count, _ = Student.objects.filter(
        year_of_study=5
    ).delete()

    print(f"Видалено записів: {deleted_count}")


# 4. Отримання студентів у зворотному порядку
def get_students_descending():
    students = Student.objects.order_by('-year_of_study')

    return students