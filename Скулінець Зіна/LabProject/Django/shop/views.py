from django.shortcuts import render
from .forms import RegistrationForm, FeedbackForm

# 1. Головна сторінка
def index(request):
    return render(request, 'shop/index.html')

# 2. Сторінка "Про нас"
def about(request):
    return render(request, 'shop/about.html')

def products(request):
    items = [
        {"name": "Ноутбук", "price": 1500, "stock": 10},
        {"name": "Смартфон", "price": 800, "stock": 15},
        {"name": "Навушники", "price": 200, "stock": 50},
        {"name": "Планшет", "price": 400, "stock": 0},
    ]
    return render(request, "shop/products.html", {"items": items})

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

    return render(request, 'shop/register.html', {'form': form, 'message': message})


from django import forms
from django.core.exceptions import ValidationError

class RegistrationForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=20,
        label="Ім'я користувача"
    )
    email = forms.EmailField(label="Електронна пошта")
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Пароль"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label="Підтвердіть пароль"
    )

    # Перевірка збігу паролів
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Паролі не збігаються!")

        return cleaned_data

    def feedback(request):
        success = False
        if request.method == "POST":
            form = FeedbackForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                with open("feedback.txt", "a", encoding="utf-8") as f:
                    f.write(f"Full Name: {data['full_name']}\n")
                    f.write(f"Email: {data['email']}\n")
                    f.write(f"Message: {data['message']}\n")
                    f.write(f"Rating: {data['rating']}\n")
                    f.write("-" * 20 + "\n")
                success = True

                form = FeedbackForm()
        else:
            form = FeedbackForm()

        return render(request, 'shop/feedback.html', {'form': form, 'success': success})