from django import forms
class FeedbackForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', required=False)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=False)
    rating = forms.IntegerField(label='Rating', min_value=1, max_value=5,
     widget=forms.NumberInput(attrs={'class': 'rating-input'}), required=False)