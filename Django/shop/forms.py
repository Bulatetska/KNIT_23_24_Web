from django import forms
from django.core.exceptions import ValidationError

class RegistrationForm(forms.Form):
    username = forms.CharField(
        min_length=3, 
        max_length=20, 
        label="Ім'я користувача"
    )
    email = forms.EmailField(label="Електронна пошта")
    password = forms.CharField(
        widget=forms.PasswordInput, 
        label="Пароль"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, 
        label="Підтвердіть пароль"
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # Перевірка на збіг паролів
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Паролі не збігаються!")
        
        return cleaned_data
