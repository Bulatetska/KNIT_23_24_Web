from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author_name', 'content']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок поста'}),
            'author_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше ім’я'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст публікації'}),
        }
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'content']
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ім’я'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Напишіть коментар...'}),
        }