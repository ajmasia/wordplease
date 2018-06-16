"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from core.api import UsersAPI, UserDetailAPI
from core.views import signup, BlogsListView, LoginView
from posts.views import UserPostList, NewPostView, UserPostDetail, PostList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('', PostList.as_view(), name='home'),
    path('blogs/', BlogsListView.as_view(), name='blogs'),
    path('blogs/<str:username>/', UserPostList.as_view(), name ='user-blog'),
    path('blogs/<str:username>/<int:pk>/', UserPostDetail.as_view(), name ='post-detail'),
    path('new-post/', NewPostView.as_view(), name='new-post'),

    # API URLs
    path('api/v1/users/', UsersAPI.as_view(), name='api-users'),
    path('api/v1/users/<int:pk>', UserDetailAPI.as_view(), name='api-user-detail'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
