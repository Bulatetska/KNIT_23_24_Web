from django.http import HttpResponse

def index(request):
    return HttpResponse("Система профілів користувачів")

def users(request):
    return HttpResponse("Список користувачів: Іван, Марія, Олег")

def userDetails(request,username):
    return HttpResponse(f"Користувач: {username}")

def userOrders(request,username):
    return HttpResponse(f"Замовлення користувача: {username}")