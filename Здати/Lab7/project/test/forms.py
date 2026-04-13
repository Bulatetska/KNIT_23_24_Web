from django import forms
class FeedbackForm(forms.Form):
    full_name = forms.CharField(min_length=3, max_length=20, label="Ім'я")
    email = forms.EmailField(label="Пошта")
    message = forms.CharField(
        label="Повідомлення",
        widget=forms.Textarea(attrs={
            'placeholder': 'Напишіть ваш відгук тут'
        }))
    rating = forms.IntegerField(label="Оцінка", widget=forms.NumberInput(attrs={'class': 'rating-input'}))
    
