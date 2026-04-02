from django import forms

class FeedbackForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Введіть ваше повідомлення"})
    )
    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={"class": "rating-input"})
    )