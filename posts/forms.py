from django import forms

from categories.models import Category
from posts.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        # Use model
        model = Post

        # Show fields
        fields = ['title', 'snippet_text', 'body', 'image', 'publication_date', 'categories']

        def __init__(self, user, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            self.fields['categories'].queryset = Category.objects.filter(owner=user)

