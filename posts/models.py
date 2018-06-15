from django.contrib.auth.models import User
from django.db import models

from categories.models import Category


class Post(models.Model):

    """
    Categories data model per user/blog
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    snippet_text = models.CharField(max_length=300)
    body = models.TextField()
    image = models.FileField()
    publication_date = models.DateTimeField()
    categories = models.ManyToManyField(Category)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Define like an object is showed in admin panel
        :return: category name
        """
        return '{0}'.format(self.title)