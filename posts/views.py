from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView

from posts.forms import PostForm
from posts.models import Post


@login_required
def new_post(request):
    if request.method == 'POST':

        form = PostForm(request.user, request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('blogs')
    else:

        form = PostForm(request)

    return render(request, 'posts/test.html', {'form': form})


class UserPostList(ListView):
    model = Post
    template_name = 'posts/list.html'

    def get_queryset(self):
        result = super().get_queryset()
        blog_user = self.kwargs.get('username')
        user = get_object_or_404(User, Q(username=blog_user))

        if self.request.user.is_authenticated:
            return result.filter(owner=user.id).order_by('-publication_date')[:10]
        else:
            return result.filter(owner=user.id, status=Post.PUBLISHED).order_by('-publication_date')[:10]


@method_decorator(login_required, name='dispatch')
class NewPostView(View):
    """
    New post view class
    """

    def get(self, request):
        form = PostForm()

        context = {'form': form}
        return render(request, 'posts/new_post.html', context)

    def post(self, request):
        # Define new instance
        post = Post()

        # Add user logged
        post.owner = request.user

        # Create form
        form = PostForm(request.POST, request.FILES, instance=post)

        # Validate form
        if form.is_valid():
            # Create add
            post = form.save()

            # Clear form
            form = PostForm()

            # Redirect
            return redirect('blogs')

        context = {'form': form}
        return render(request, 'posts/new_post.html', context)


class UserPostDetail(View):

    def get(self, request, username, pk):
        """
        Show post detail
        :param request: HttpRequest object
        :param pk: username, pk
        :return: HttpResponse
        """

        try:
            post = Post.objects.get(owner__username=username, pk=pk)

        except Post.DoesNotExist:
            return HttpResponse('Post don´t exist in database', status=404)

        context = {'post': post}

        return render(request, 'posts/detail.html', context)


class PostList(ListView):
    queryset = Post.objects.filter(status=Post.PUBLISHED)
    template_name = 'posts/list.html'

    def get_queryset(self):
        result = super().get_queryset()
        return result.order_by('-publication_date')[:10]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'WordPlease'
        context['claim'] = 'Our last published posts'
        return context