from django.shortcuts import render
from django.http import JsonResponse

def users(request):
    data = [
        {"name": "Іван", "age": 25},
        {"name": "Марія", "age": 30}
    ]
    return JsonResponse(data, safe=False)

def user_detail(request, name):
    user = {
        "name": name,
        "age": 25,
        "orders": ["Ноутбук", "Смартфон"]
    }
    return JsonResponse(user)
