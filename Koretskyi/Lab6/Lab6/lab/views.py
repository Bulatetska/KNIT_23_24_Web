from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm

def register(request):
    message = ""
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            message = "Реєстрація була успішна"
        else:
            message = "Дані некоректні"

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form, 'message': message})
