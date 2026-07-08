from django import forms

class FeedbackForm(forms.Form):
    full_name = forms.CharField(
        label="Повне ім'я",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Введіть ваше ім\'я'})
    )
    email = forms.EmailField(
        label="Email",
        required=False,
        widget=forms.EmailInput(attrs={'placeholder': 'example@mail.com'})
    )
    message = forms.CharField(
        label="Повідомлення",
        widget=forms.Textarea(attrs={'placeholder': 'Напишіть ваш відгук тут...', 'rows': 4})
    )
    rating = forms.IntegerField(
        label="Рейтинг (1-5)",
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'class': 'rating-input', 'style': 'border: 2px solid #4CAF50;'})
    )
