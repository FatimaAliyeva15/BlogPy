from django import forms
from .models import BlogPost

class BlogPostForms(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']