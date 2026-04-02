from email.policy import HTTP
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("система профілів користувачів")
def user_list(request):
    return HttpResponse("Список користувачів: Іван, Марія, Олег")
def user_details(request,username):
    return HttpResponse(f"Користувач: {username}")
def user_orders(request, username):
    return HttpResponse(f"Замовлення користувача:{username}")