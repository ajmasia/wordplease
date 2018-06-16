import json

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView


class UsersAPI(APIView):

    def get(self, request):

        """
        Return users list
        :param request: HttpRequest object
        :return: HttpResponse object
        """

        users = User.objects.all()

        response = []
        for user in users:
            response.append({
                'username': user.username,
                'firs_name': user.first_name,
                'last_name': user.last_name,
                'blog_name': user.profile.blog_name,
                'blog_description': user.profile.blog_description
            })

        return Response(response)
