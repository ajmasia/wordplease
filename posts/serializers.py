from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostSerializerList(ModelSerializer):

    class Meta:

        model = Post
        fields = '__all__'
