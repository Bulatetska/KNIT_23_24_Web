from django.shortcuts import render
from django.shortcuts import render
from .forms import FeedbackForm
from django.shortcuts import render

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            with open('feedback.txt', 'a', encoding='utf-8') as f:
                f.write(f"Full Name: {data['full_name']}\n")
                f.write(f"Email: {data.get('email') or 'Not provided'}\n")
                f.write(f"Message: {data['message']}\n")
                f.write(f"Rating: {data['rating']}\n")
                f.write("-" * 10 + "\n")  
                
            form = FeedbackForm() 
            return render(request, 'feedback.html', {'form': form, 'success': True})
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})
