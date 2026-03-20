from django.http import JsonResponse

users = {
    "Іван": {"name": "Іван", "age": 25, "orders": ["Ноутбук", "Смартфон"]},
    "Марія": {"name": "Марія", "age": 30, "orders": ["Планшет", "Навушники"]},
}

def user_list(request):
    data = [{"name": u["name"], "age": u["age"]} for u in users.values()]
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

def user_detail(request, name):
    user = users.get(name)
    if user:
        return JsonResponse(user, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({"error": "Користувача не знайдено"}, status=404, json_dumps_params={'ensure_ascii': False})