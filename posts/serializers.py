from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostListSerializer(ModelSerializer):

    class Meta:

        model = Post
        fields = ['id', 'title', 'snippet_text', 'image']


class NewPostSerializer(ModelSerializer):

    class Meta:

        model = Post
        fields = ['title', 'snippet_text', 'body', 'image', 'publication_date', 'categories']


class PostDetailSerializer(ModelSerializer):

    class Meta:

        model = Post
        fields = '__all__'

