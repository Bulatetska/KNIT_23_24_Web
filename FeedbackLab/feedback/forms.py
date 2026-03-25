from django import forms

class FeedbackForm(forms.Form):
    full_name = forms.CharField(
        required=True,
        label="Full Name"
    )

    email = forms.EmailField(
        required=False,
        label="Email"
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Введіть ваше повідомлення...'
        }),
        label="Message"
    )

    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={
            'class': 'rating-input'
        }),
        label="Rating (1-5)"
    )