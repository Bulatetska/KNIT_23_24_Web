from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def users(request):
    data = [
        {"name": "Іван", "age": 25},
        {"name": "Марія", "age": 30}
        {"name": "Олег", "age": 24}
        {"name": "Артур", "age": 18}
        {"name": "Артем", "age": 19}
    ]
    return JsonResponse(data, safe=False)

def user_detail(request, name):
    data = {
        "name":Іван ,
        "age": 25,
        "orders": ["Ноутбук", "Смартфон"]
    }
    return JsonResponse(data)