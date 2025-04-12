from django import forms

class FeedbackForm(forms.Form):
    full_name = forms.CharField(
        label='Full Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Введіть своє ім’я та прізвище'})
    )
    email = forms.EmailField(
        label='Email',
        required=False,
        widget=forms.EmailInput(attrs={'placeholder': 'Введіть email'})
    )
    message = forms.CharField(
        label='Message',
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Ваш відгук або повідомлення'})
    )
    rating = forms.IntegerField(
        label='Rating',
        required=True,
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'class': 'rating-input', 'placeholder': 'Оцініть від 1 до 5'})
    )