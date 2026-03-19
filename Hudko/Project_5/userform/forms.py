from django import forms

class UserForm(forms.Form):
    name = forms.CharField(
        required=True,
        min_length=3,
        max_length=20,
        label="Ім'я користувача"
        )
    
    email = forms.EmailField(
        required=True,
        label="Електронна пошта"
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label="Пароль"
    )
    
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label="Підтвердіть Пароль"
        )
    
    def clean(self):
        cleaned_data = super().clean()
        
        if cleaned_data.get('password') != cleaned_data.get('confirm_password'):
            raise forms.ValidationError("Passwords invalid")
        
        return cleaned_data;