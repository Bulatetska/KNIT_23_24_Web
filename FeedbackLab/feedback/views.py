from django.shortcuts import render
from django.shortcuts import render
from .forms import FeedbackForm

def feedback(request):
    errors = []
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
                f.write("\n-----------------\n")

            success = True
        else:
            errors = form.errors.values()
    else:
        form = FeedbackForm()

    return render(request, "feedback.html", {
        "form": form,
        "errors": errors,
        "success": success
    })