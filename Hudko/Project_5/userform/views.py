from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def register(request):
    message = ""
    
    if request.method == "POST":
        userform = UserForm(request.POST)
        
        if userform.is_valid():
            message = "Успішна реєстрація"
        else:
            message = "Дані не коректні"
    else:
        userform = UserForm()
        
    return render(request, "index.html", {"form": userform , "message":message})