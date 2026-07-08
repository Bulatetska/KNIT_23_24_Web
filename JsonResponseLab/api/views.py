from django.http import JsonResponse

def get_users(request):
    data = [
        {"name": "Ivan", "age": 25},
        {"name": "Maria", "age": 30}
    ]
    # Додаємо json_dumps_params, щоб вимкнути ASCII-кодування
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

def get_user_detail(request, name):
    data = {
        "name": name,
        "age": 25,
        "orders": ["Ноутбук", "Смартфон"]
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})