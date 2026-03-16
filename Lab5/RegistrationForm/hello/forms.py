from django import forms
class UserForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())