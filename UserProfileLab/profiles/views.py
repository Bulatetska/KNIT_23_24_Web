from django.http import HttpResponse

def home(request):
    return HttpResponse("Система профілів користувачів")

def user_list(request):
    return HttpResponse("Список користувачів: Іван, Марія, Олег")

def user_detail(request, username):
    return HttpResponse(f"Користувач: {username}")

def user_orders(request, username):
    return HttpResponse(f"Замовлення користувача: {username}")