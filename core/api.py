import json

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from core.serializers import UserSerializerList, UserSerializer


class UsersAPI(GenericAPIView):

    queryset = User.objects.all()

    def get_serializer_class(self):
        return UserSerializer if self.request.method == 'POST' else UserSerializerList

    def get(self, request):

        """
        Return users list
        :param request: HttpRequest object
        :return: HttpResponse object
        """

        queryset = self.queryset
        users = self.paginate_queryset(queryset)
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(users, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request):

        """
        Create new user and return new user info
        :param request:
        :return:
        """

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return  Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserDetailAPI(GenericAPIView):

    def get_serializer_class(self):
        return UserSerializer if self.request.method == 'POST' else UserSerializerList

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

    def delete(self, request, pk):

        """
        Delete user
        :param request:
        :param pk:
        :return:
        """

        user = get_object_or_404(User, pk=pk)
        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):

        """
        Update user
        :param request:
        :param pk:
        :return:
        """

        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        else:
            return  Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

