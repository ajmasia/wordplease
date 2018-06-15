from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):

    """
    Categories data model per user/blog
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name_plural = 'Categories'

    def __str__(self):
        """
        Define like an object is showed in admin panel
        :return: category name
        """
        return '{0}'.format(self.name)