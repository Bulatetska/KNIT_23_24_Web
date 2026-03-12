# register/views.py
from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Получаем очищенные данные
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            rating = form.cleaned_data['rating']

            # Сохраняем в файл (относительно корня проекта)
            with open('feedback.txt', 'a', encoding='utf-8') as f:
                f.write(f"Full Name: {full_name}\n")
                f.write(f"Email: {email}\n")
                f.write(f"Message: {message}\n")
                f.write(f"Rating: {rating}\n")
                f.write("-" * 30 + "\n")

            # Можно добавить сообщение об успехе или редирект
            return render(request, 'register/feedback.html', {'form': form, 'success': True})
    else:
        form = FeedbackForm()

    return render(request, 'register/feedback.html', {'form': form})