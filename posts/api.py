from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
from posts.serializers import PostSerializerList


class PostListAPI(APIView):

    def get(self, request):
        """

        :param request:
        :return:
        """
        posts = Post.objects.all()
        serializer = PostSerializerList(posts, many=True)

        return Response(serializer.data)