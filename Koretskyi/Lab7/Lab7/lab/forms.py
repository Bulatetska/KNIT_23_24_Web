from django import forms

class FeedBackForm(forms.Form):
    full_name = forms.CharField(required=True,label="Full Name")
    email = forms.EmailField(required=False,label="Email")
    message = forms.CharField(label="Message", widget=forms.Textarea, help_text="Напишіть ваше повідомлення")
    rating = forms.IntegerField(label="Rating",min_value=1,max_value=5,
                                widget=forms.NumberInput(attrs={'class':'rating-input'}))