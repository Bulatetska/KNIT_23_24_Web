from django.test import TestCase

from .models import Course, Student
from .student_services import (
    check_student_exists,
    create_default_students,
    delete_graduated_students,
    get_long_courses_as_dict,
    get_student_count_by_year,
    get_students_ordered_by_year_desc,
    get_students_with_year_above_two_raw,
    get_third_year_students,
    update_student_year,
)


class StudentServicesTest(TestCase):
    def test_create_default_students(self):
        create_default_students()

        self.assertEqual(Student.objects.count(), 2)
        self.assertTrue(Student.objects.filter(student_id="S123456789").exists())
        self.assertTrue(Student.objects.filter(student_id="S987654321").exists())

    def test_update_student_year(self):
        create_default_students()

        updated_count = update_student_year("S123456789", 4)

        self.assertEqual(updated_count, 1)
        self.assertEqual(
            Student.objects.get(student_id="S123456789").year_of_study,
            4,
        )

    def test_delete_graduated_students(self):
        create_default_students()
        update_student_year("S987654321", 5)

        deleted_count = delete_graduated_students()

        self.assertEqual(deleted_count, 1)
        self.assertFalse(Student.objects.filter(student_id="S987654321").exists())

    def test_get_students_ordered_by_year_desc(self):
        create_default_students()
        update_student_year("S123456789", 4)

        students = list(get_students_ordered_by_year_desc())

        self.assertEqual(
            [student.student_id for student in students],
            ["S123456789", "S987654321"],
        )

    def test_get_third_year_students(self):
        create_default_students()

        students = list(get_third_year_students())

        self.assertEqual(
            students,
            [{"full_name": "Марія Петренко", "year_of_study": 3}],
        )

    def test_check_student_exists(self):
        create_default_students()

        self.assertEqual(
            check_student_exists("S123456789"),
            "Студент з номером квитка S123456789 існує.",
        )
        self.assertEqual(
            check_student_exists("S000000000"),
            "Студента з номером квитка S000000000 не знайдено.",
        )

    def test_get_student_count_by_year(self):
        create_default_students()
        Student.objects.create(
            full_name="Ірина Коваль",
            year_of_study=3,
            student_id="S111111111",
        )

        grouped_data = list(get_student_count_by_year())

        self.assertEqual(
            grouped_data,
            [
                {"year_of_study": 2, "total": 1},
                {"year_of_study": 3, "total": 2},
            ],
        )

    def test_get_students_with_year_above_two_raw(self):
        create_default_students()
        Student.objects.create(
            full_name="Ірина Коваль",
            year_of_study=4,
            student_id="S111111111",
        )

        students = list(get_students_with_year_above_two_raw())

        self.assertEqual(
            [student.student_id for student in students],
            ["S987654321", "S111111111"],
        )

    def test_get_long_courses_as_dict(self):
        Course.objects.create(course_name="Python Basics", duration_hours=80)
        Course.objects.create(course_name="Django Advanced", duration_hours=120)
        Course.objects.create(course_name="Databases", duration_hours=140)

        courses = get_long_courses_as_dict()

        self.assertEqual(
            courses,
            [
                {"course_name": "Databases", "duration_hours": 140},
                {"course_name": "Django Advanced", "duration_hours": 120},
            ],
        )
