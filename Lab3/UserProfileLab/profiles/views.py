from django.http import HttpResponse

def index(request):
    return HttpResponse("Система профілів користувачів")

def users(request):
    return HttpResponse("Список користувачів: Іван, Марія, Олег")

def username(request, username):
    return HttpResponse(f"Користувач: {username}")

def orders(request, username):
    return HttpResponse(f"Замовлення користувача: {username}") 