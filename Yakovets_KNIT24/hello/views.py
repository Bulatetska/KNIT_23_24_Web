from django.http import HttpResponse, JsonResponse

# Завдання 1: Система профілів
def home(request):
    return HttpResponse("<h1>Система профілів користувачів</h1>")

def user_list(request):
    return HttpResponse("Список користувачів: Іван, Марія, Олег")

def user_detail(request, username):
    return HttpResponse(f"Користувач: {username}")

def user_orders(request, username):
    return HttpResponse(f"Замовлення користувача: {username}")

# Завдання 2: Магазин
def shop_home(request):
    return HttpResponse("Ласкаво просимо до нашого магазину")

def category_view(request, category):
    return HttpResponse(f"Категорія: {category}")

def product_view(request, category, product):
    return HttpResponse(f"Товар: {product} у категорії {category}")

def sale_view(request):
    return HttpResponse("Акційні товари магазину")

# Завдання 3: JSON API
def get_users_json(request):
    data = [
        {"name": "Іван", "age": 25},
        {"name": "Марія", "age": 30}
    ]
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

def get_user_detail_json(request, name):
    data = {
        "name": name,
        "age": 25,
        "orders": ["Ноутбук", "Смартфон"]
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})

# Завдання 4: Система курсів
def course_list(request):
    return HttpResponse("Доступні курси: Python, Django, Machine Learning")

def course_detail(request, course_name):
    return HttpResponse(f"Курс: {course_name}")

def module_list(request, course_name):
    return HttpResponse(f"Модулі курсу {course_name}: Модуль 1, Модуль 2")

def module_detail(request, course_name, module_id):
    return HttpResponse(f"Модуль {module_id} курсу {course_name}")