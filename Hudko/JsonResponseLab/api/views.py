from django.shortcuts import render
from django.http import JsonResponse
data = [
        {"name": "Іван", "age": 25},
        {"name": "Марія", "age": 30}
    ]

def users(request):
    return JsonResponse(data,safe=False,json_dumps_params={'ensure_ascii': False})

def userDetails(request, name):
    user = next((user for user in data if user.get("name") == name), None)
    
    res = user or {"name": name, "age": 25}
    
    return JsonResponse(res,safe=False,json_dumps_params={'ensure_ascii': False})