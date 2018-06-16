from django import forms
from django.core.exceptions import ValidationError

from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        # Use model
        model = Post

        # Show fields
        fields = ['title', 'snippet_text', 'body', 'image', 'publication_date', 'categories']

    # Specific field validation
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image is not None and 'image' not in image.content_type:
            raise ValidationError('The file is not an image')
        return image
