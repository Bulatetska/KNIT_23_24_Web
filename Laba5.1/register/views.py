from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return HttpResponse("Успішна реєстрація")
        else:
            return HttpResponse("Дані некоректні")
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})