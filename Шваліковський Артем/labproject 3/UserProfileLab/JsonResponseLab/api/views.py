from django.http import JsonResponse

users = {
    "Іван": {
        "name": "Іван",
        "age": 25,
        "orders": ["Ноутбук", "Смартфон"]
    },

    "Марія": {
        "name": "Марія",
        "age": 30,
        "orders": ["Навушники", "Планшет"]
    }
}

def users_list(request):

    data = [
        {"name": "Іван", "age": 25},
        {"name": "Марія", "age": 30}
    ]

    return JsonResponse(data, safe=False)


def user_detail(request, name):

    user = users.get(name)

    if user:
        return JsonResponse(user)

    return JsonResponse(
        {"error": "Користувача не знайдено"},
        status=404
    )