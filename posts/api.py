from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from posts.models import Post
from posts.permissions import PostPermissions
from posts.serializers import PostListSerializer, PostDetailSerializer, NewPostSerializer


class PostListAPI(ListCreateAPIView):
    """
    Posts list endpoint
    """
    queryset = Post.objects.all().filter(status=Post.PUBLISHED)
    permission_classes = [PostPermissions]

    def get_serializer_class(self):
        return NewPostSerializer if self.request.method == 'POST' else PostListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Post detail endpoint
    """
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [PostPermissions]


class UserPostListAPI(ListCreateAPIView):

    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        if self.request.user.is_authenticated:
            return Post.objects.filter(owner=self.request.user)
        else:
            return Post.objects.filter(owner=self.request.user, status=Post.PUBLISHED)
