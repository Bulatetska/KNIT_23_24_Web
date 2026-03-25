from django.shortcuts import render
from .forms import RegistrationForm, FeedbackForm


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

    return render(request, "registration/register.html", {
        "form": form,
        "message": message
    })


def feedback(request):
    message = ""
    errors = []

    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            full_name = form.cleaned_data["full_name"]
            email = form.cleaned_data["email"]
            feedback_message = form.cleaned_data["message"]
            rating = form.cleaned_data["rating"]

            with open("feedback.txt", "a", encoding="utf-8") as file:
                file.write(f"Full Name: {full_name}\n")
                file.write(f"Email: {email}\n")
                file.write(f"Message: {feedback_message}\n")
                file.write(f"Rating: {rating}\n\n")

            message = "Дані успішно збережено"
            form = FeedbackForm()
        else:
            message = "Дані некоректні"
            for field, field_errors in form.errors.items():
                for error in field_errors:
                    errors.append(f"{field}: {error}")
    else:
        form = FeedbackForm()

    return render(request, "registration/feedback.html", {
        "form": form,
        "message": message,
        "errors": errors
    })
