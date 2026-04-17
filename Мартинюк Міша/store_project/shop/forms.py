from django import forms
from django.core.exceptions import ValidationError


class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=20, label='Ім\'я користувача')
    email = forms.EmailField(label='Електронна пошта')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Підтвердження пароля')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError('Пароль і підтвердження пароля не збігаються.')

        return cleaned_data


class FeedbackForm(forms.Form):
    full_name = forms.CharField(required=True, label="Повне ім'я")
    email = forms.EmailField(required=False, label='Електронна пошта')
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Введіть ваш відгук або повідомлення'}),
        label='Повідомлення',
    )
    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        label='Оцінка',
        widget=forms.NumberInput(attrs={'class': 'rating-input'}),
    )
