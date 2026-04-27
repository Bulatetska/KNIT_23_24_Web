from django.shortcuts import render

# Create your views here.
# feedback/views.py

from django.shortcuts import render
from .forms import FeedbackForm

def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            with open("feedback.txt", "a", encoding="utf-8") as f:
                f.write(f"Full Name: {data['full_name']}\n")
                f.write(f"Email: {data.get('email', '')}\n")
                f.write(f"Message: {data['message']}\n")
                f.write(f"Rating: {data['rating']}\n")
                f.write("----------------------\n")

    else:
        form = FeedbackForm()

    return render(request, "feedback.html", {"form": form})