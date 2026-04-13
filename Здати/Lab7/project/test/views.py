from django.shortcuts import render
from django.http import HttpResponse
from .forms import FeedbackForm



def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            try:
                with open('feedback.txt', 'a', encoding='utf-8') as f:
                    f.write(f"Full Name: {data['full_name']}\n")
                    f.write(f"Email: {data.get('email', 'N/A')}\n")
                    f.write(f"Message: {data['message']}\n")
                    f.write(f"Rating: {data['rating']}\n")
                    f.write("-" * 20 + "\n")
                
                return HttpResponse("Дякуємо за ваш відгук!")
            except IOError:
                return HttpResponse("Помилка при збереженні даних", status=500)
    else:
        form = FeedbackForm()

    return render(request, 'test/feedback.html', {'form': form})