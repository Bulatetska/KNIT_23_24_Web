from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password")
        p2 = cleaned_data.get("confirm_password")
        if p1 != p2:
            self.add_error('confirm_password', "Паролі не збігаються!")
        return cleaned_data