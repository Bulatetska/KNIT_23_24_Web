from django import forms
class UserForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea(), help_text='Input your message')
    rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'class':'rating-input'}))
    required_css_class="field"
    error_css_class = "error"