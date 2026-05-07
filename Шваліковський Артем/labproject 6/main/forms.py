from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=20,
        label="Ім'я користувача"
    )

    email = forms.EmailField(label="Email")

    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Пароль"
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label="Підтвердіть пароль"
    )

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Паролі не співпадають!")

        return cleaned_data