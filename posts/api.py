from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
from posts.serializers import PostSerializerList, PostDetailSerializer, NewPostSerializer


# class PostListAPI(APIView):
#
#     def get(self, request):
#         """
#
#         :param request:
#         :return:
#         """
#         posts = Post.objects.all()
#         serializer = PostSerializerList(posts, many=True)
#
#         return Response(serializer.data)

class PostListAPI(ListCreateAPIView):
    """
    Posts list endpoint
    """
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        return NewPostSerializer if self.request.method == 'POST' else PostSerializerList

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Post detail endpoint
    """
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
