from django import forms

class FeedbackForm(forms.Form):
    full_name = forms.CharField(
        max_length=100, 
        required=True, 
        label="Повне ім'я"
    )
    email = forms.EmailField(
        required=False, 
        label="Електронна пошта"
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Введіть ваше повідомлення тут...'}),
        label="Повідомлення"
    )
    rating = forms.IntegerField(
        min_value=1, 
        max_value=5, 
        widget=forms.NumberInput(attrs={'class': 'rating-input'}),
        label="Рейтинг (від 1 до 5)"
    )