from django.shortcuts import render
from django.views import View

from posts.forms import NewPostForm


class NewPostView(View):

    """
    New post view class
    """

    def get(self, request):

        form = NewPostForm()

        context = {'form': form}
        return render(request, 'posts/new_post.html', context)