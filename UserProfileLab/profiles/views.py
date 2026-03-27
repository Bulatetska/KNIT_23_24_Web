from django.http import HttpResponse

_users = {
    "Tom": {"orders": ["Order1", "Order2"]},
    "Lisa": {"orders": ["Order3"]},
    "Bob": {"orders": []}
}

def index(request):
    return HttpResponse("Система профілів користувачів.")

def users(request):
    names = ", ".join(_users.keys())
    return HttpResponse("Список користувачів: " + names)

def user(request, username):
    if username in _users:
        return HttpResponse(f"Користувач: {username}")
    return HttpResponse("Користувача не знайдено")

def orders(request, username):
    if username in _users:
        orders = _users[username]["orders"]
        return HttpResponse(f"Замовлення користувача: {', '.join(orders)}")
    return HttpResponse("Користувача не знайдено")
