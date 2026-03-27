from django.shortcuts import render
from django.shortcuts import render
from .forms import RegistrationForm

def register(request):
    message = ""
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            message = "Успішна реєстрація"
        else:
            message = "Дані некоректні"
    else:
        form = RegistrationForm()

    return render(request, "register.html", {"form": form, "message": message})
def about(request):
    return render(request, "about.html")
def home(request):
    return render(request, "index.html",)