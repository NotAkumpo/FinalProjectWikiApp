from django import forms
from .models import ArticleCategory, Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'entry': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'header_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']
        widgets = {
            'entry': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }