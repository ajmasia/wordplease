from django.contrib import admin
from django.contrib.admin import register
from posts.models import Post


# Admin panel customize
@register(Post)
class PostAdmin(admin.ModelAdmin):
    autocomplete_fields = ['owner']
    list_display = ['title', 'owner_blog_name', 'owner']
    list_filter = ['title', 'owner']
    search_fields = ['owner_blog_name', 'owner']

    # Define a method to show first_name & last_name
    def owner_blog_name(self, item):
        return '{0}'.format(item.owner.profile.blog_name)

    # Order by owner_name
    # Define attribute order to owner_name method with order field value
    owner_blog_name.admin_order_field = 'owner__username'

    # Define header label
    owner_blog_name.short_description = 'Blog\'s name'

    readonly_fields = ['created_on', 'updated_on']