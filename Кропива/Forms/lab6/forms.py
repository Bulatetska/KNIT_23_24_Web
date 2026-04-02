from django import forms

class FeedbackForm(forms.Form):
    full_name = forms.CharField(
        label="Full Name",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your full name'
        })
    )

    email = forms.EmailField(
        label="Email",
        required=False,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email (optional)'
        })
    )

    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Write your feedback here...',
            'rows': 4
        })
    )

    rating = forms.IntegerField(
        label="Rating",
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={
            'class': 'form-control rating-input'
        })
    )