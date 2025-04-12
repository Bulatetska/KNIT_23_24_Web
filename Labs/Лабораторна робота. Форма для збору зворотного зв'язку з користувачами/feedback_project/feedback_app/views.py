import os
from django.shortcuts import render
from .forms import FeedbackForm
from django.conf import settings

def feedback(request):
    errors = []
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            rating = form.cleaned_data['rating']

            # Формування тексту у форматі YAML
            feedback_text = (
                f"Full Name: {full_name}\n"
                f"Email: {email}\n"
                f"Message: {message}\n"
                f"Rating: {rating}\n"
            )

            # Визначте шлях до файлу. Наприклад, файл зберігатиметься в директорії проекту.
            file_path = os.path.join(settings.BASE_DIR, 'feedback.txt')

            # Збереження даних до файлу (доповнення до файлу, або перезапис, в залежності від потреб)
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(feedback_text + "\n")  # Додаємо перенесення рядка між записами

            # Можна відобразити повідомлення або перенаправити на іншу сторінку
            return render(request, 'feedback.html', {'form': FeedbackForm(), 'message': 'Дякуємо за ваш відгук!'})
        else:
            errors = form.errors.get_json_data(escape_html=True)
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form, 'errors': errors})