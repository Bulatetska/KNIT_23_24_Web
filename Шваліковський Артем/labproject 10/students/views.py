from django.shortcuts import render
from .models import Student, Course
from .utils import *


def dashboard(request):
    return render(request, "students/dashboard.html")


def third_year_students_view(request):
    students = Student.objects.filter(year_of_study=3).values(
        'full_name', 'year_of_study'
    )

    return render(request, "students/third_year.html", {
        "students": students
    })


def check_student_view(request):

    result = None

    if request.method == "POST":
        student_id = request.POST.get("student_id")
        result = check_student_exists(student_id)

    return render(request, "students/check_student.html", {
        "result": result
    })


def stats_view(request):

    data = students_group_by_year()

    return render(request, "students/stats.html", {
        "data": data
    })


def courses_view(request):

    courses = long_courses_dict()

    return render(request, "students/courses.html", {
        "courses": courses
    })