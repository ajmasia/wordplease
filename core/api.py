import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View


class UsersAPI(View):

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
                'last_name': user.last_name
            })

        return HttpResponse(json.dumps(response))
