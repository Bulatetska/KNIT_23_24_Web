from django.core.management.base import BaseCommand

from shop.models import Course, Student
from shop.student_services import (
    check_student_exists,
    create_default_students,
    get_long_courses_as_dict,
    get_student_count_by_year,
    get_students_with_year_above_two_raw,
    get_third_year_students,
    update_student_year,
)


class Command(BaseCommand):
    help = "Demonstrates advanced Django ORM queries for students and courses"

    def handle(self, *args, **options):
        Student.objects.all().delete()
        Course.objects.all().delete()

        create_default_students()
        update_student_year("S123456789", 4)

        Student.objects.update_or_create(
            student_id="S111111111",
            defaults={
                "full_name": "Ірина Коваль",
                "year_of_study": 3,
                "student_id": "S111111111",
            },
        )

        Course.objects.update_or_create(
            course_name="Python Basics",
            defaults={"duration_hours": 80},
        )
        Course.objects.update_or_create(
            course_name="Django Advanced",
            defaults={"duration_hours": 120},
        )
        Course.objects.update_or_create(
            course_name="Databases",
            defaults={"duration_hours": 140},
        )

        self.stdout.write(self.style.SUCCESS("Студенти 3 курсу (тільки ПІБ і рік навчання):"))
        for student in get_third_year_students():
            self.stdout.write(f"- {student['full_name']} | курс {student['year_of_study']}")

        self.stdout.write(self.style.WARNING("Перевірка наявності студента за номером квитка:"))
        self.stdout.write(f"- {check_student_exists('S987654321')}")
        self.stdout.write(f"- {check_student_exists('S000000000')}")

        self.stdout.write(self.style.HTTP_INFO("Кількість студентів на кожному курсі:"))
        for item in get_student_count_by_year():
            self.stdout.write(f"- Курс {item['year_of_study']}: {item['total']} студент(и)")

        self.stdout.write(self.style.WARNING("Результат SQL через raw() для студентів з роком навчання > 2:"))
        for student in get_students_with_year_above_two_raw():
            self.stdout.write(
                f"- {student.full_name}, курс {student.year_of_study}, квиток {student.student_id}"
            )

        self.stdout.write(self.style.SUCCESS("Курси тривалістю більше 100 годин:"))
        for course in get_long_courses_as_dict():
            self.stdout.write(
                f"- {{'course_name': '{course['course_name']}', 'duration_hours': {course['duration_hours']}}}"
            )
