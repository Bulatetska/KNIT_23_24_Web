from tkinter import E
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def courses(request):
    return HttpResponse("Доступні курси: Python, Django, Machine Learning")
def course_details(request,course_name):
    return HttpResponse(f"Курс: {course_name}")
def modules(request, course_name):
    return HttpResponse(f"Модулі курсу {course_name}Модуль 1, Модуль 2")
def modules_details(request, course_name, module_id):
    return HttpResponse(f"Модуль {module_id} курсу {course_name}")