from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
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

        form = PostForm()

    return render(request, 'posts/new_post.html', {'form': form})


class UserBlog(ListView):
    model = Post
    template_name = 'posts/list.html'

    def get_queryset(self):
        result = super().get_queryset()
        blog_user = self.kwargs.get('username')
        user = get_object_or_404(User, Q(username=blog_user))
        return result.filter(owner=user.id)[:5]
