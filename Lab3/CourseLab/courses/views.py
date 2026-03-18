from django.http import HttpResponse

def index(request):
 return HttpResponse("Доступні курси: Python, Django, Machine Learning")
def course_name(request, course_name):
 return HttpResponse(f"Курс: {course_name}")
def module(request, course_name):
 return HttpResponse(f"Модулі курсу {course_name}: Модуль 1, Модуль 2")
def module_id(request, course_name, module_id):
    return HttpResponse(f"Модуль {module_id} курсу {course_name}")
     