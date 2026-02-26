from django.http import JsonResponse

users_data = [
    {"name": "Іван", "age": 25},
    {"name": "Марія", "age": 30},
]

def users_list(request):
    return JsonResponse(users_data, safe=False)

def user_detail(request, name):
    user_info = {
        "name": name,
        "age": 25,
        "orders": ["Ноутбук", "Смартфон"]
    }
    return JsonResponse(user_info)