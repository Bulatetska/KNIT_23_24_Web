from django.shortcuts import render
from .forms import FeedbackForm
import os

def feedback(request):
    success_message = ""

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            with open('feedback.txt', 'a', encoding='utf-8') as f:
                f.write(f"Full Name: {data['full_name']}\n")
                f.write(f"Email: {data.get('email', '')}\n")
                f.write(f"Message: {data['message']}\n")
                f.write(f"Rating: {data['rating']}\n")
                f.write("-" * 20 + "\n")
            
            success_message = "Ваш відгук успішно збережено!"
            form = FeedbackForm() 
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form, 'success_message': success_message})