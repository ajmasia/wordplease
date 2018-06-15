from django.contrib import admin
from django.contrib.admin import register
from categories.models import Category


# Admin panel customize
@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    autocomplete_fields = ['owner']
    list_display = ['name', 'owner_blog_name', 'owner']
    list_filter = ['name', 'owner']
    search_fields = ['name', 'owner__username']

    # Define a method to show first_name & last_name
    def owner_blog_name(self, item):
        return '{0}'.format(item.owner.profile.blog_name)

    # Order by owner_name
    # Define attribute order to owner_name method with order field value
    owner_blog_name.admin_order_field = 'owner__first_name'

    # Define header label
    owner_blog_name.short_description = 'Blog\'s name'

    readonly_fields = ['created_on', 'updated_on']

    # Change titles
    admin.site.site_header = 'WordPlease Admin'
    admin.site.site_title = 'WordPlease Admin'
    admin.site.index_title = 'Dashboard'