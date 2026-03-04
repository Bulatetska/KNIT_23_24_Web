from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Система профілів користувачів")
def users(request):
    return HttpResponse("Список користувачів: Іван, Марія, Олег")
def users_detail(request):
    return HttpResponse(f"Користувач: {users}")
def users_orders(request):
    return HttpResponse(f"Замовлення користувача: {users}")

# Create your views here.
