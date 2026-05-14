from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author_name', 'content']
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше ім’я'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваш відгук', 'rows': 3}),
        }