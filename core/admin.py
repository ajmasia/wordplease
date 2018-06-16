from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from core.models import Profile

# Define an inline admin descriptor for CustomUser model


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (
        ProfileInLine,
    )


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)