from django.test import TestCase

from .models import Student
from .student_services import (
    create_default_students,
    delete_graduated_students,
    get_students_ordered_by_year_desc,
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
