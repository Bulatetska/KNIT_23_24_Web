from django import forms

class FeedbackForm(forms.Form):
    full_name = forms.CharField(
        label="Повне ім'я",
        required=True
    )
    email = forms.EmailField(
        label="Електронна пошта",
        required=False  # Поле необов'язкове
    )
    message = forms.CharField(
        label="Повідомлення",
        widget=forms.Textarea(attrs={'placeholder': 'Введіть ваше повідомлення тут...'})
    )
    rating = forms.IntegerField(
        label="Рейтинг (1-5)",
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'class': 'rating-input'})
    )