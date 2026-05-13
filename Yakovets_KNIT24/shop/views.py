from django.http import JsonResponse
from .models import Student

def create_students(request):
    Student.objects.create(full_name="Олександр Іваненко", study_year=2, student_card="S123456789")
    Student.objects.create(full_name="Марія Петренко", study_year=3, student_card="S987654321")
    return JsonResponse({"status": "created"})

def update_year(request, card):
    student = Student.objects.filter(student_card=card).first()
    if student:
        student.study_year += 1
        student.save()
        return JsonResponse({"status": "updated"})
    return JsonResponse({"status": "not found"})


def remove_graduates(request):
    Student.objects.filter(study_year=5).delete()
    return JsonResponse({"status": "graduates removed"})


def sorted_students(request):
    students = Student.objects.order_by("-study_year")
    data = list(students.values())
    return JsonResponse(data, safe=False)
