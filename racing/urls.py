from django.contrib import admin
from rest_framework import routers
from django.conf.urls import url
from racing.views import biker_views, auth_views, post_views, comment_views

router = routers.DefaultRouter()

urlpatterns = [
    url('auth/sign_up', auth_views.SignUp.as_view()),

    url('biker/list$', biker_views.BikerListAllView.as_view()),
    url('biker/create$', biker_views.BikerCreateView.as_view()),

    url('post/list$', post_views.PostListAllView.as_view()),
    url('post/create$', post_views.PostCreateView.as_view()),

    url('comment/list$', comment_views.CommentListView.as_view()),

    url('admin/', admin.site.urls),
]
