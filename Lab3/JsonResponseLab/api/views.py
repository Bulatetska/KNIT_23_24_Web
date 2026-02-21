from django.shortcuts import render
from django.http import JsonResponse

def user_list(request):
    return JsonResponse([
    {"name": "Peter", "age": 60},
    {"name": "Stepan", "age": 20},
], safe=False)

def user_info(request, username):
    if username == "Peter":
        return JsonResponse({'name': 'Peter', 'age': 60, 'orders': ['laptop','headphones']}, safe=False)
    elif username == "Stepan":
        return JsonResponse({'name': 'Stepan', 'age': 20, 'orders': ['TV','tablet']}, safe=False)

# Create your views here.
