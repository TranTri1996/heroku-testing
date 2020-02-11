from rest_framework import routers
from django.conf.urls import url
from racing.views import biker_views, post_views
from rest_framework_jwt.views import obtain_jwt_token
router = routers.DefaultRouter()

urlpatterns = [
    url('^biker/account/register$', biker_views.BikerRegisterView.as_view()),
    url('^biker/account/login$', obtain_jwt_token),
    url('^biker/account/profile$', biker_views.BikerGetProfileView.as_view()),

    url('^biker/list$', biker_views.BikerListAllView.as_view()),

    url('^post/list$', post_views.PostListAllView.as_view()),
    url('^post/create$', post_views.PostCreateView.as_view()),
]
