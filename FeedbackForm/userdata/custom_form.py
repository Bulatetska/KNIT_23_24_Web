from django import forms

class FeedbackForm(forms.Form):
    full_name = forms.CharField(label="Full Name", required=True)
    email = forms.EmailField(label="Email", required=False)
    message = forms.CharField(
        label="Message",
        required=True,
        widget=forms.Textarea()
    )
    rating = forms.IntegerField(
        label="Rating",
        required=True,
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'class': 'rating-input'})
    )