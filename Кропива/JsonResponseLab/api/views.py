from django.http import JsonResponse

users = [
    {"name": "Іван", "age": 25},
    {"name": "Марія", "age": 30}
]

user_orders = {
    "Іван": ["Ноутбук", "Смартфон"],
    "Марія": ["Планшет"]
}


def users_list(request):
    return JsonResponse(users, safe=False, json_dumps_params={'ensure_ascii': False})


def user_detail(request, name):
    user = next((u for u in users if u["name"] == name), None)

    if user:
        data = {
            "name": user["name"],
            "age": user["age"],
            "orders": user_orders.get(name, [])
        }
        return JsonResponse(data)

    return JsonResponse({"error": "Користувача не знайдено"})


from django.shortcuts import render

# Create your views here.
