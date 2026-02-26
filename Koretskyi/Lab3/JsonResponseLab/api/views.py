from django.http import JsonResponse

users = [
    {"name": "Іван", "age": 25},
    {"name": "Марія", "age": 30},
]
def users_list(request):
    return JsonResponse(users, safe=False)

def user_detail(request,name):
    data = {
        "name": name,
        "age": 25,
        "orders": ["Ноутбук", "Смартфон"]
    }
    return JsonResponse(data)