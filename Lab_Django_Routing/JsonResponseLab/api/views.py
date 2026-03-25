from django.http import JsonResponse

users = [
    {"name": "Іван", "age": 25},
    {"name": "Марія", "age": 30},
]

user_details = {
    "Іван": {
        "name": "Іван",
        "age": 25,
        "orders": ["Ноутбук", "Смартфон"]
    },
    "Марія": {
        "name": "Марія",
        "age": 30,
        "orders": ["Планшет", "Навушники"]
    }
}

def users_list(request):
    return JsonResponse(users, safe=False)

def user_detail(request, name):
    return JsonResponse(user_details.get(name, {"error": "not found"}))
