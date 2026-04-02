from django.shortcuts import render
from .forms import RegistrationForm


def register(request):
    message = None

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            message = " Успішна реєстрація!"
        else:
            message = " Дані некоректні"
    else:
        form = RegistrationForm()

    return render(request, "register.html", {
        "form": form,
        "message": message
    })