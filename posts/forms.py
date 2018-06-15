from django.forms import ModelForm, forms

from posts.models import Post


class NewPostForm(ModelForm):

    class Meta:
        # Use model
        model = Post

        # Show fields
        fields = '__all__'

        # Exclude fields
        exclude = ['created_on', 'updated_on']

        def __init__(self, *args, **kwargs):
            super(NewPostForm, self).__init__(*args, **kwargs)
            self.fields['categories'].widget = forms.widgets.CheckboxSelectMultiple()
