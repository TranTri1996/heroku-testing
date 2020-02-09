from rest_framework import routers
from django.conf.urls import url
from racing.views import biker_views, post_views

router = routers.DefaultRouter()

urlpatterns = [
    url('^biker/account/register$', biker_views.BikerRegisterView.as_view()),
    url('^biker/account/login$', biker_views.BikerLoginView.as_view()),
    url('^biker/account/logout$', biker_views.BikerLogoutView.as_view()),
    url('^biker/account/profile$', biker_views.BikerGetProfileView.as_view()),

    url('^biker/list$', biker_views.BikerListAllView.as_view()),

    url('^post/list$', post_views.PostListAllView.as_view()),
    url('^post/create$', post_views.PostCreateView.as_view()),
]
