from django.http import JsonResponse
USERS_LIST = {
    "Іван": {"name": "Іван", "age": 25, "orders": ["Ноутбук", "Смартфон"]},
    "Марія": {"name": "Марія", "age": 30, "orders": ["Книга", "Квіти"]}
}
def users_list(request):
    data = [
        {"name": "Іван", "age": 25},
        {"name": "Марія", "age": 30}
    ]
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
def user_detail(request, name):
    user_data = USERS_LIST.get(name)
    if user_data:
        return JsonResponse(user_data, safe=False, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse({"error": "Користвача не знайдено"}, status=400, json_dumps_params={'ensure_ascii': False})


