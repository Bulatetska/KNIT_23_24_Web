from django import forms
from django.core.exceptions import ValidationError

# Форма з минулої частини лаби
class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=20, label="Логін")
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Підтвердіть пароль")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Паролі не збігаються!")
        return cleaned_data


class FeedbackForm(forms.Form):
    full_name = forms.CharField(label="Повне ім'я", required=True)
    email = forms.EmailField(label="Email", required=False)
    message = forms.CharField(
        label="Повідомлення",
        widget=forms.Textarea(attrs={'placeholder': 'Напишіть ваш відгук тут...'})
    )
    rating = forms.IntegerField(
        label="Рейтинг (1-5)",
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'class': 'rating-input'})
    )