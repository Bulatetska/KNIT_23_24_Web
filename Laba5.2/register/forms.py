# register/forms.py
from django import forms

class FeedbackForm(forms.Form):
    full_name = forms.CharField(
        label='Повне имя',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Кравчук Сергій'})
    )
    email = forms.EmailField(
        label='Email',
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com'})
    )
    message = forms.CharField(
        label='Повідомлення',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваше повідовлення...', 'rows': 12})
    )
    rating = forms.IntegerField(
        label='Оцінка',
        min_value=1,
        max_value=12,
        widget=forms.NumberInput(attrs={'class': 'rating-input form-control'})
    )