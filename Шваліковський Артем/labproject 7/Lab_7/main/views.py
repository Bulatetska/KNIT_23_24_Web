from django.shortcuts import render
from .forms import FeedbackForm

def feedback(request):
    message = ""
    errors = []

    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            with open("feedback.txt", "a", encoding="utf-8") as file:
                file.write(f"Full Name: {data['full_name']}\n")
                file.write(f"Email: {data['email']}\n")
                file.write(f"Message: {data['message']}\n")
                file.write(f"Rating: {data['rating']}\n")
                file.write("\n-----------------\n\n")

            message = "Дані успішно збережено!"
            form = FeedbackForm()

        else:
            errors = form.errors.values()

    else:
        form = FeedbackForm()

    return render(request, "feedback.html", {
        "form": form,
        "message": message,
        "errors": errors
    })