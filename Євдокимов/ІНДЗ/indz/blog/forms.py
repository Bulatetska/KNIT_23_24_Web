from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author_name']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Заголовок поста'}),
            'content': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Текст поста', 'rows': 6}),
            'author_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ваше ім\'я'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'content']
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ваше ім\'я'}),
            'content': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Ваш коментар', 'rows': 3}),
        }