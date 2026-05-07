from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("Система профілів користувачів")

def users_list(request):
    return HttpResponse("Список користувачів: Іван, Марія, Олег, Артур, Артем")

def user_detail(request, username):
    return HttpResponse(f"Користувач: {username}")

def user_orders(request, username):
    return HttpResponse(f"Замовлення користувача: {username}")