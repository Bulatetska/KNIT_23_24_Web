from django.http import HttpResponse

data = {
    "Python": {"Модуль 1": "Тест тест тест", "Модуль 2": "Тест тест тест", "Модуль 3": "Тест тест тест"},
    "Django": {"Модуль 1": "Тест тест тест", "Модуль 2": "Тест тест тест", "Модуль 3": "Тест тест тест", "Модуль 4": "Тест тест тест"},
    "Machine Learning": {"Модуль 1": "Тест тест тест", "Модуль 2": "Тест тест тест", "Модуль 3": "Тест тест тест"},
}

def courses(request):
    return HttpResponse("Доступні курси: Python, Django, Machine Learning")

def name(request, course_name):
    if course_name not in data:
        return HttpResponse(f"Курсу {course_name} немає")
    return HttpResponse(f"Курс: {course_name}")


def modules(request, course_name):

    if course_name not in data:
        return HttpResponse(f"Курсу {course_name} немає", status=404)

    course_modules = data[course_name]

    module_names = ", ".join(course_modules.keys())

    return HttpResponse(f"Модулі курсу {course_name}: {module_names}")

def details(request, course_name, module_id):
    if course_name not in data:
        return HttpResponse(f"Курсу {course_name} немає", status=404)
    course_modules = data[course_name]
    if module_id not in course_modules:
        return HttpResponse(f"Модуль {module_id} відсутній в курсі {course_name}", status=404)

    output = course_modules[module_id]

    return HttpResponse(output, status=200)