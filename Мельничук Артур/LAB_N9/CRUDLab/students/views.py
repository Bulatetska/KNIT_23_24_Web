from django.http import HttpResponse
from .crud import (create_students, update_year,
                   delete_graduated, get_students_sorted)
from .models import Student


def index(request):
    # Створюємо студентів
    create_students()

    # Оновлюємо рік навчання
    update_year("S123456789", 3)

    # Отримуємо відсортований список
    students = get_students_sorted()

    result = ""
    for student in students:
        result += f"{student.full_name} -- рік {student.year_of_study}<br>"

    return HttpResponse(f"<h1>Студенти:</h1>{result}")


def delete_view(request):
    delete_graduated()
    return HttpResponse("Студентів 5-го року видалено!")


