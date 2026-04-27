from django.core.management.base import BaseCommand
import random
from students.models import Student, Course


class Command(BaseCommand):
    help = 'Заповнення бази студентами'

    def handle(self, *args, **kwargs):
        names = [
            "Іван Петренко",
            "Марія Іваненко",
            "Олег Шевченко",
            "Анна Коваль",
            "Дмитро Бондар",
            "Олена Мельник",
            "Андрій Ткаченко",
            "Наталія Савчук"
        ]

        # очищаємо базу
        Student.objects.all().delete()
        Course.objects.all().delete()

        # створюємо студентів (УНІКАЛЬНІ квитки)
        for i in range(30):
            Student.objects.create(
                full_name=random.choice(names),
                year=random.randint(1, 4),
                ticket_number=f"STU-{1000 + i}"
            )

        # курси
        Course.objects.create(name="Python", hours=120)
        Course.objects.create(name="Java", hours=90)
        Course.objects.create(name="Data Science", hours=150)

        self.stdout.write(self.style.SUCCESS("✅ Дані створено"))