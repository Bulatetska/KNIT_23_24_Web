from django.http import JsonResponse

users = [
    {"name": "Іван", "age": 25, "orders": ["Ноутбук", "Смартфон"]},
    {"name": "Марія", "age": 30, "orders": ["Планшет", "Навушники"]},
]

def users_list(request):
    data = [{"name": u["name"], "age": u["age"]} for u in users]
    return JsonResponse(data, safe=False)

def user_detail(request, name):
    for user in users:
        if user["name"] == name:
            return JsonResponse(user)
    return JsonResponse({"error": "Користувача не знайдено"}, status=404)