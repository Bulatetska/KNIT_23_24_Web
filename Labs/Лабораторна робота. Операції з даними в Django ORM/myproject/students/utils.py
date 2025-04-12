from .models import Student

def create_students():
    # Створення запису для Олександра Іваненка
    student1 = Student.objects.create(
        full_name='Олександр Іваненко',
        year=2,
        student_card='S123456789'
    )
    # Створення запису для Марії Петренко
    student2 = Student.objects.create(
        full_name='Марія Петренко',
        year=3,
        student_card='S987654321'
    )
    print("Студентські записи створено!")
    
def update_student_year(student_card, new_year):
    try:
        student = Student.objects.get(student_card=student_card)
        student.year = new_year
        student.save()
        print(f"Рік навчання студента {student.full_name} оновлено на {new_year}.")
    except Student.DoesNotExist:
        print("Студент з таким номером студентського квитка не знайдений.")

def delete_finished_students():
    finished_students = Student.objects.filter(year=5)
    count = finished_students.count()
    finished_students.delete()
    print(f"Видалено {count} студент(ів), які закінчили навчання.")

def get_students_sorted_desc():
    students = Student.objects.all().order_by('-year')
    return students

# Додаткова функція для друку результатів:
def print_sorted_students():
    students = get_students_sorted_desc()
    for student in students:
        print(f"{student.full_name} - Рік навчання: {student.year}")