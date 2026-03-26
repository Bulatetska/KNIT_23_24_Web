from .models import Student


def create_default_students():
    students_data = [
        {
            "full_name": "Олександр Іваненко",
            "year_of_study": 2,
            "student_id": "S123456789",
        },
        {
            "full_name": "Марія Петренко",
            "year_of_study": 3,
            "student_id": "S987654321",
        },
    ]

    created_students = []
    for student_data in students_data:
        student, _ = Student.objects.update_or_create(
            student_id=student_data["student_id"],
            defaults=student_data,
        )
        created_students.append(student)

    return created_students


def update_student_year(student_id, new_year):
    updated_count = Student.objects.filter(student_id=student_id).update(
        year_of_study=new_year
    )
    return updated_count


def delete_graduated_students():
    deleted_count, _ = Student.objects.filter(year_of_study=5).delete()
    return deleted_count


def get_students_ordered_by_year_desc():
    return Student.objects.order_by("-year_of_study", "full_name")
