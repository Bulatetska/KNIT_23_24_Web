from django.shortcuts import render
from .forms import FeedbackForm


def feedback_view(request):
    if request.method == 'POST':
        # Якщо користувач натиснув кнопку "Надіслати"
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Записуємо у файл feedback.txt (формат з image_9759da.png)
            with open('feedback.txt', 'a', encoding='utf-8') as f:
                f.write(f"Full Name: {data['full_name']}\n")
                f.write(f"Email: {data['email']}\n")
                f.write(f"Message: {data['message']}\n")
                f.write(f"Rating: {data['rating']}\n")
                f.write("-" * 20 + "\n")

            # Після успіху можна знову дати порожню форму
            form = FeedbackForm()
    else:
        # Якщо користувач просто зайшов на сторінку
        form = FeedbackForm()

    return render(request, 'feedback/form_template.html', {'form': form})