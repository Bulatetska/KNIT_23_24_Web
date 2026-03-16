from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse
def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            rating = form.cleaned_data['rating']
            with open('feetback.txt', 'a') as f:
                f.write(f'Full Name: {full_name}\n')
                f.write(f'Email: {email}\n')
                f.write(f'Message: {message}\n')
                f.write(f'Rating: {rating}\n')
            return HttpResponse('Feedback is written')
        else:
            return render(request, form.errors)
    else:
        form = UserForm()
        return render(request, 'index.html', {'form': form})
# Create your views here.
