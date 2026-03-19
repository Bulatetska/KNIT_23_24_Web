from django.shortcuts import render
from django.http import HttpResponse
from .custom_forms import RegistrationForm

def index(request):
    registration_form = RegistrationForm()
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        message = ""
        if registration_form.is_valid():
            message = f"Успішна реєстрація"
        else:
            message = "Дані некоректні"
        return render(request, 'index.html', {'form': registration_form, 'message': message})

    return render(request, 'index.html', {"form": registration_form})