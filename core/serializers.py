from rest_framework import serializers


class UserSerializerList(serializers.Serializer):

    id = serializers.ReadOnlyField()
    username = serializers.CharField()


class UserSerializer(UserSerializerList):

    first_name = serializers.CharField()
    last_name = serializers.CharField()