from django import forms

class FeedbackForm(forms.Form):
    full_name = forms.CharField(label="Full Name", required=True)
    email = forms.EmailField(label="Email", required=True)
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={'placeholder': 'Ваш відгук тут'})
    )
    rating = forms.IntegerField(
        label="Rating",
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'class': 'rating-input'})
    )
