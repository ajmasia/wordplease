import json

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from core.serializers import UserSerializerList, UserSerializer


class UsersAPI(APIView):

    def get(self, request):

        """
        Return users list
        :param request: HttpRequest object
        :return: HttpResponse object
        """

        users = User.objects.all()
        serializer = UserSerializerList(users, many=True)

        return Response(serializer.data)

class UserDetailAPI(APIView):

    def get(self, request, pk):

        """
        Endpoint user detail
        :param request: HttpRequest object
        :param pk: pk
        :return: HttpResponse object
        """

        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)