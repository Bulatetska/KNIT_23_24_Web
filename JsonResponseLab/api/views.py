from django.shortcuts import render
from django.http import JsonResponse
data = [

  {"name": "Іван", "age": 25},

  {"name": "Марія", "age": 30}
]
def user(request):
    return JsonResponse(data, safe=False,json_dumps_params={'ensure_ascii':False})
def user_name(request,name):
    return JsonResponse({

  "name": name,

  "age": 25,

  "orders": ["Ноутбук", "Смартфон"]

},json_dumps_params={'ensure_ascii':False})