from django.shortcuts import render
from .forms import FeedbackForm
import yaml
import os

def feedback(request):
    form = FeedbackForm(request.POST or None)
    errors = None

    if request.method == "POST":
        if form.is_valid():
            # Отримуємо очищені дані
            data = form.cleaned_data

            # Підготовка даних у форматі YAML
            yaml_data = yaml.dump({
                "Full Name": data.get("full_name"),
                "Email": data.get("email"),
                "Message": data.get("message"),
                "Rating": data.get("rating"),
            }, allow_unicode=True, default_flow_style=False)

            # Збереження у файл feedback.txt (додати нові записи)
            file_path = os.path.join(os.path.dirname(__file__), "feedback.txt")
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(yaml_data)
                f.write("\n---\n")  # Роздільник між записами

            # Повернення повідомлення про успіх
            return render(request, "feedback_success.html", {"data": data})
        else:
            errors = form.errors  # Збираємо список помилок

    return render(request, "feedback.html", {"form": form, "errors": errors})