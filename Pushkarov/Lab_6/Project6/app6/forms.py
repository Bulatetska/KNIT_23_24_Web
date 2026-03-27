from django import forms
class UserForm(forms.Form):
 name = forms.CharField(min_length=3, max_length=20)
 email = forms.EmailField()
 password = forms.CharField(widget=forms.PasswordInput)
 confirm_password = forms.CharField(widget=forms.PasswordInput)
 def clean(self):
    if self.cleaned_data.get('password') != self.cleaned_data.get('confirm_password'):
        raise forms.ValidationError("Passwords invalid")
    return self.cleaned_data