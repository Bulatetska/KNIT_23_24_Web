from django.db.models import Count

from .models import Course, Student


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


def get_third_year_students():
    return Student.objects.filter(year_of_study=3).values("full_name", "year_of_study")


def check_student_exists(student_id):
    if Student.objects.filter(student_id=student_id).exists():
        return f"Студент з номером квитка {student_id} існує."
    return f"Студента з номером квитка {student_id} не знайдено."


def get_student_count_by_year():
    return Student.objects.values("year_of_study").annotate(total=Count("id")).order_by(
        "year_of_study"
    )


def get_students_with_year_above_two_raw():
    sql = (
        "SELECT id, full_name, year_of_study, student_id "
        "FROM shop_student WHERE year_of_study > %s"
    )
    return Student.objects.raw(sql, [2])


def get_long_courses_as_dict():
    return list(
        Course.objects.filter(duration_hours__gt=100)
        .values("course_name", "duration_hours")
        .order_by("course_name")
    )
