from django.shortcuts import render
from .forms import FeedbackForm

def feedback(request):
    form = FeedbackForm()
    message = ""
    errors = []

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            with open("feedback.txt", "a", encoding="utf-8") as f:
                f.write(f"Full Name: {data['full_name']}\n")
                f.write(f"Email: {data['email']}\n")
                f.write(f"Message: {data['message']}\n")
                f.write(f"Rating: {data['rating']}\n")
                f.write("---\n")
            message = "Дякуємо за відгук!"
        else:
            errors = form.errors

    return render(request, "feedback.html", {"form": form, "message": message, "errors": errors})