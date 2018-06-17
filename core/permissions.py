from rest_framework.permissions import BasePermission


class UserPermissions(BasePermission):

    def has_permission(self, request, view):
        """
        Define user permissions
        :param request:
        :param view:
        :return:
        """

        from core.api import UserDetailAPI

        if request.method == 'POST':
            return True

        if request.user.is_authenticated and (
                request.method != 'POST' or request.user.is_superuser or isinstance(view, UserDetailAPI)
        ):
            return True

        return False

    def has_object_permission(self, request, view, obj):
        """
        Define object user permissions
        :param request:
        :param view:
        :param obj:
        :return:
        """

        return request.user.is_superuser or request.user == obj
