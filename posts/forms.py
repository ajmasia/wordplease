from django import forms
from django.core.exceptions import ValidationError

from categories.models import Category
from posts.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        # Use model
        model = Post

        # Show fields
        fields = ['title', 'snippet_text', 'body', 'image', 'publication_date', 'categories']
