from django.shortcuts import render
from .forms import FeedBackForm

def feedback(request):
    errors = []
    success = False
    if request.method == "POST":
        form = FeedBackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            with open("feedback.txt", "a",encoding="utf-8") as f:
                f.write(f"Full Name {data['full_name']}\n")
                f.write(f"Email {data['email']}\n")
                f.write(f"Message {data['message']}\n")
                f.write(f"Rating {data['rating']}\n")
                f.write("'\n")
            success = True
            form = FeedBackForm()
        else:
            errors = form.errors.values()
    else:
        form = FeedBackForm()
    return render(request, "feedback.html", {"form": form, "errors": errors, "success": success})