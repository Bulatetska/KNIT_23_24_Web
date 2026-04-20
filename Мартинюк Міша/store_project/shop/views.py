from pathlib import Path

from django.shortcuts import render

from .forms import FeedbackForm, RegistrationForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def register(request):
    message = ''

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            message = 'Успішна реєстрація'
            form = RegistrationForm()
        else:
            message = 'Дані некоректні'
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form, 'message': message})


def feedback(request):
    message = ''

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            feedback_path = Path(__file__).resolve().parent.parent / 'feedback.txt'
            feedback_path.write_text(
                f"Full Name: {cleaned_data['full_name']}\n\n"
                f"Email: {cleaned_data.get('email', '')}\n\n"
                f"Message: {cleaned_data['message']}\n\n"
                f"Rating: {cleaned_data['rating']}\n",
                encoding='utf-8',
            )
            message = 'Відгук успішно збережено'
            form = FeedbackForm()
        else:
            message = 'Дані некоректні'
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form, 'message': message})


def products(request):
    items = [
        {"name": "Ноутбук", "price": 1500, "stock": 10},
        {"name": "Смартфон", "price": 800, "stock": 15},
        {"name": "Навушники", "price": 200, "stock": 0},
    ]
    return render(request, 'products.html', {'items': items})
