from django.shortcuts import HttpResponse

def courses_list(request):
    return HttpResponse("Доступні курси: Python, Django, Machine Learning")

def course_detail(request, course_name):
    return HttpResponse(f"Курс: {course_name}")

def course_modules(request, course_name):
    return HttpResponse(f"Модулі курсу {course_name}: Модуль 1, Модуль 2")

def module_detail(request, course_name, module_id):
    return HttpResponse(f"Модуль {module_id} курсу {course_name}")
