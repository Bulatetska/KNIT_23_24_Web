from django.core.management.base import BaseCommand

from shop.student_services import (
    create_default_students,
    delete_graduated_students,
    get_students_ordered_by_year_desc,
    update_student_year,
)


class Command(BaseCommand):
    help = "Demonstrates creating, updating, sorting, and deleting student records"

    def handle(self, *args, **options):
        created_students = create_default_students()
        self.stdout.write(self.style.SUCCESS("Створено або оновлено студентів:"))
        for student in created_students:
            self.stdout.write(
                f"- {student.full_name}, курс {student.year_of_study}, квиток {student.student_id}"
            )

        updated_count = update_student_year("S123456789", 4)
        self.stdout.write(
            self.style.WARNING(
                f"Оновлено записів для S123456789: {updated_count}. Новий рік навчання: 4"
            )
        )

        update_student_year("S987654321", 5)
        self.stdout.write(self.style.WARNING("Студента S987654321 переведено на 5 курс для демонстрації видалення."))

        self.stdout.write(self.style.HTTP_INFO("Студенти, відсортовані за роком навчання у зворотному порядку:"))
        for student in get_students_ordered_by_year_desc():
            self.stdout.write(
                f"- {student.full_name}, курс {student.year_of_study}, квиток {student.student_id}"
            )

        deleted_count = delete_graduated_students()
        self.stdout.write(self.style.ERROR(f"Видалено студентів 5 курсу: {deleted_count}"))
