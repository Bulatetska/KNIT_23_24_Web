from .models import Student, Course


def seed_data():

    # STUDENTS
    Student.objects.get_or_create(
        full_name="Олександр Іваненко",
        year_of_study=2,
        student_id="S123456789"
    )

    Student.objects.get_or_create(
        full_name="Марія Петренко",
        year_of_study=3,
        student_id="S987654321"
    )

    Student.objects.get_or_create(
        full_name="Артем Олександрович",
        year_of_study=2,
        student_id="S111111111"
    )

    Student.objects.get_or_create(
        full_name="Анна Петрівна",
        year_of_study=3,
        student_id="S222222222"
    )

    Student.objects.get_or_create(
        full_name="Петро Павлович",
        year_of_study=5,
        student_id="S555555555"
    )


    # COURSES
    Course.objects.get_or_create(course_name="Math", duration_hours=120)
    Course.objects.get_or_create(course_name="Physics", duration_hours=80)
    Course.objects.get_or_create(course_name="Programming", duration_hours=150)
    Course.objects.get_or_create(course_name="History", duration_hours=60)
    Course.objects.get_or_create(course_name="Blender", duration_hours=130)

    print("Базові дані додано!")