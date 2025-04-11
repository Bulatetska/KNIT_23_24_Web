from django.shortcuts import render
from .forms import RegistrationForm

def register(request):
    message = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            message = 'Успішна реєстрація'
            # Тут можна зберегти дані або виконати інші дії
        else:
            message = 'Дані некоректні'
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form, 'message': message})