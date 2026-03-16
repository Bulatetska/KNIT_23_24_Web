from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse
def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password != confirm_password:
                return HttpResponse('Некоректні дані: паролі не співпадають')
            else:
                return HttpResponse('Успішна реєстрація')
        else:
            return HttpResponse('Некоректні дані: ' + str(form.errors))
    else:
        form = UserForm()
        return render(request, 'index.html', {'form': form})
