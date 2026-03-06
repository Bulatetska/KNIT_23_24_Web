from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=20,label="Ім’я")
    email = forms.EmailField(label="Пошта")
    password = forms.CharField(widget=forms.PasswordInput(render_value=False), label="Пароль")
    confirm_password = forms.CharField(widget=forms.PasswordInput(render_value=False), label="Підтвердити пароль")
    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Неправильно введено пароль!!!")

        return cleaned_data