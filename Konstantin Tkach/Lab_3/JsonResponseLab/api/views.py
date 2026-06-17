from django.http import JsonResponse


def users_list(request):
    users = [
        {"name": "Іван", "age": 25},
        {"name": "Марія", "age": 30}
    ]
    return JsonResponse(users, safe=False)


def user_detail(request, name):
    users_data = {
        "Іван": {"name": "Іван", "age": 25, "orders": ["Ноутбук", "Смартфон"]},
        "Марія": {"name": "Марія", "age": 30, "orders": ["Книга", "Сумка"]}
    }

    if name in users_data:
        return JsonResponse(users_data[name])
    else:
        return JsonResponse({"error": "Користувача не знайдено"}, status=404)