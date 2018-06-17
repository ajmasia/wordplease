from django.contrib import messages
from django.contrib.auth import login as django_login, authenticate
from django.shortcuts import render, redirect


# @login_required
from django.views import View
from django.views.generic import ListView

from core.forms import SignUpForm, LoginForm
from core.models import Profile


def signup(request):

    if request.method == 'POST':

        form = SignUpForm(request.POST)

        if form.is_valid():

            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.blog_name = form.cleaned_data.get('blog_name')
            user.profile.blog_description = form.cleaned_data.get('blog_description')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            django_login(request, user)

            # Get next url parameter
            url = request.GET.get('next', 'home')

            # Redirect user
            return redirect(url)
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})


class LoginView(View):

    """
    Login view class
    """

    def get(self, request):
        """
        Show login form
        :param request: HttpRequest object
        :return: HttpResponse object with rendered login form
        """

        form = LoginForm()

        context = {'form': form}
        return render(request, 'core/login.html', context)

    def post(self, request):
        """
        Procces access data
        :param request: HttpRequest object
        :return: HttpResponse object with rendered login form
        """

        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Check if credential access are ok
            user = authenticate(username=username, password=password)

            if user is None:
                # Show error message
                messages.error(request, "Ops! Incorrect credentials!")
            else:
                # Start authenticate user session
                django_login(request, user)

                # Get next url parameter
                url = request.GET.get('next', 'blogs')

                # Redirect user
                return redirect(url)

        context = {'form': form}
        return render(request, 'core/login.html', context)


class BlogsListView(ListView):

    """
    Blogs list generic view class
    """

    # Queryset from CustomUser data model
    queryset = Profile.objects.all()

    # View template
    template_name = 'blogs/list.html'

    # Getting queryset
    def get_queryset(self):
        result = super().get_queryset()
        return result

    # Getting custom context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Available blogs'
        context['claim'] = 'You can read all these blogs in WordPlease'
        return context