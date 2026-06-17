from django import forms


class FeedbackForm(forms.Form):
    # Обов'язкове текстове поле
    full_name = forms.CharField(label="Full Name", required=True)

    # Необов'язкове поле для email
    email = forms.EmailField(label="Email", required=False)

    # Багаторядкове поле (Textarea) з підказкою всередині
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={'placeholder': 'Введіть ваше повідомлення...'})
    )

    # Числове поле від 1 до 5 з кастомним CSS-класом
    rating = forms.IntegerField(
        label="Rating",
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'class': 'rating-input'})
    )