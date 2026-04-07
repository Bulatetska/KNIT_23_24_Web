from django.shortcuts import render
from .custom_form import FeedbackForm


def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            with open('feedback.txt', 'a') as f:
                f.write(f"Full Name: {data['full_name']}\n")
                f.write(f"Email: {data['email']}\n")
                f.write(f"Message: {data['message']}\n")
                f.write(f"Rating: {data['rating']}\n")

            return render(request, 'index.html', {'form': FeedbackForm(), 'success': True})
    else:
        form = FeedbackForm()

    return render(request, 'index.html', {'form': form})