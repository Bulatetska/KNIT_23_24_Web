from django.shortcuts import render
from .forms import FeedbackForm

def feedback(request):
    form = FeedbackForm()
    feedback_data = None
    errors = None

    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            feedback_data = form.cleaned_data

            # Збереження у файл
            with open('feedback.txt', 'a', encoding='utf-8') as f:
                f.write(f"Full Name: {feedback_data['full_name']}\n")
                f.write(f"Email: {feedback_data['email']}\n")
                f.write(f"Message: {feedback_data['message']}\n")
                f.write(f"Rating: {feedback_data['rating']}\n")
                f.write("\n-----------------\n")

            # очищаємо форму після відправки
            form = FeedbackForm()

        else:
            errors = form.errors

    return render(request, 'feedback.html', {
        'form': form,
        'feedback_data': feedback_data,
        'errors': errors
    })