from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):

    blog_name = forms.CharField(max_length=300)
    blog_description = forms.CharField(max_length=300)

    class Meta:
        model = User
        fields = ('username', 'blog_name', 'blog_description', 'password1', 'password2', )


class LoginForm(forms.Form):

    """
    Login form class
    """

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())