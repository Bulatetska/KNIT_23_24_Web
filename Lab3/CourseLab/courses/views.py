from django.shortcuts import render
from django.http import HttpResponse

def courses(request):
    return HttpResponse("Доступні курси: Python, Django, Machine Learning")

def namecourse(request, course_name):
    courses = ['Python','Django','Machine Learning']
    if course_name in courses:
        return HttpResponse(f'Курс: {course_name}')

def modules(request, course_name):
    courses = ['Python','Django','Machine Learning']
    if course_name in courses:
        return HttpResponse(f'Модулі курсу {course_name}: Модуль1, Модуль2')

def module_details(request, course_name, module_id):
    courses = ['Python','Django','Machine Learning']
    str(module_id)
    if course_name in courses and module_id in ['1','2','3','4','5']:
        return HttpResponse(f'Модуль {module_id} курсу {course_name}')
# Create your views here.
