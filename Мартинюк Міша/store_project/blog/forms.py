from django import forms

from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "author_name"]
        labels = {
            "title": "Заголовок",
            "content": "Вміст",
            "author_name": "Ім'я автора",
        }
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Введіть заголовок поста"}),
            "content": forms.Textarea(attrs={"placeholder": "Напишіть текст поста", "rows": 8}),
            "author_name": forms.TextInput(attrs={"placeholder": "Ваше ім'я"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["author_name", "content"]
        labels = {
            "author_name": "Ваше ім'я",
            "content": "Коментар",
        }
        widgets = {
            "author_name": forms.TextInput(attrs={"placeholder": "Ваше ім'я"}),
            "content": forms.Textarea(attrs={"placeholder": "Залиште коментар", "rows": 4}),
        }
