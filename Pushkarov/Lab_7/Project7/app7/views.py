from django.shortcuts import render
from .forms import FeedbackForm
def index(request):
    errors = []
    success = False
    if request.method == 'POST':        
        form = FeedbackForm(request.POST)
        if form.is_valid():
            with open('feedback.txt', 'a') as f:
                f.write(f"Full Name: {form.cleaned_data['name']}\n")
                if form.cleaned_data['email'] == '':
                    f.write("Email: Not valid\n")
                else:
                    f.write(f"Email: {form.cleaned_data['email']}\n")
                if form.cleaned_data['message'] == '':
                    f.write("Message: Not valid\n")
                else:
                    f.write(f"Message: {form.cleaned_data['message']}\n")
                if form.cleaned_data['rating'] is None:
                    f.write("Rating: Not valid\n")
                else:
                    f.write(f"Rating: {form.cleaned_data['rating']}\n")
                f.write("-" * 40 + "\n")
            success = True
            form = FeedbackForm()
        else:
            errors = form.errors
    else:
        form = FeedbackForm()
    return render(request, 'index.html', {'form': form, 'errors': errors, 'success': success})
