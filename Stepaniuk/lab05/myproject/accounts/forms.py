from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=20)
    email = forms.EmailField()

    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")

        if password != confirm:
            raise forms.ValidationError("Паролі не збігаються")

        return cleaned_data