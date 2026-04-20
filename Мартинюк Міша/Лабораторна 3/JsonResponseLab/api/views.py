from django.http import JsonResponse

USERS = {
    "Іван": {"name": "Іван", "age": 25, "orders": ["Ноутбук", "Смартфон"]},
    "Марія": {"name": "Марія", "age": 30, "orders": ["Книга", "Навушники"]},
}


def users_list(request):
    data = [{"name": "Іван", "age": 25}, {"name": "Марія", "age": 30}]
    return JsonResponse(data, safe=False)


def user_detail(request, name):
    user = USERS.get(name, {"name": name, "age": None, "orders": []})
    return JsonResponse(user)
