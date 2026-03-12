from django import forms

class FeedbackForm(forms.Form):
    full_name = forms.CharField(
        label="Full Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-input"})
    )
    email = forms.EmailField(
        label="Email",
        required=False,
        widget=forms.EmailInput(attrs={"class": "form-input"})
    )
    message = forms.CharField(
        label="Message",
        required=True,
        widget=forms.Textarea(attrs={
            "class": "form-textarea",
            "placeholder": "Введіть ваше повідомлення тут..."
        })
    )
    rating = forms.IntegerField(
        label="Rating",
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={"class": "rating-input"})
    )