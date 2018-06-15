from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(blank=True, null=True, max_length=300)
    blog_name = models.CharField(blank=True, null=True, max_length=160)
    blog_description = models.CharField(blank=True, null=True, max_length=300)

    def __str__(self):

        """
        Define like an object is showed in admin panel
        :return: user_blog_name
        """

        return '{0}'.format(self.blog_name)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()