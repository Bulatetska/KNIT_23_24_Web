from django import forms

class FeedbackForm(forms.Form):

    full_name = forms.CharField(
        label="Full Name",
        required=True
    )

    email = forms.EmailField(
        label="Email",
        required=False
    )

    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            'placeholder': 'Введіть ваше повідомлення...',
            'rows': 5,
            'cols': 40
        })
    )

    rating = forms.IntegerField(
        label="Rating",
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={
            'class': 'rating-input'
        })
    )