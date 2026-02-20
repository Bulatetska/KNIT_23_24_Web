from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>Система профілів користувачів</h1>")
def list_users(request):
    return HttpResponse("Список користувачів: Іван, Марія, Олег")
def user_info(request, name):
    people = ['Іван','Марія','Олег']
    if name in people:
        return HttpResponse(f"<h1>Користувач: {name}</h1>")
def orders(request, name):
    people = ['Іван','Марія','Олег']
    if name in people:
        return HttpResponse(f"<h1>Замовлення користувача: {name}</h1>")
# Create your views here.
