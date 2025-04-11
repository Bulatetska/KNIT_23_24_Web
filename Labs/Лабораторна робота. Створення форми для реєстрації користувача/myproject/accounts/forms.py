from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(
        label='Імʼя користувача',
        min_length=3,
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Введіть імʼя користувача'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'Введіть email'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Введіть пароль'})
    )
    confirm_password = forms.CharField(
        label='Підтвердження пароля',
        widget=forms.PasswordInput(attrs={'placeholder': 'Підтвердіть пароль'})
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Паролі не співпадають")
        return cleaned_data
