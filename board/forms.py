from socket import fromshare
from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'contents')

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'contents')
