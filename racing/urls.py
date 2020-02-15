from rest_framework import routers
from django.conf.urls import url
from racing.views import biker_views, post_views, auth_views

router = routers.DefaultRouter()

urlpatterns = [
    url('^account/register$', auth_views.RegisterView.as_view()),
    url('^account/login$', auth_views.LoginView.as_view()),
    url('^account/logout$', auth_views.LogoutView.as_view()),
    url('^account/forgot_password$', auth_views.ForgotPasswordView.as_view()),

    url('^biker/profile$', biker_views.BikerGetProfileView.as_view()),

    url('^post/list$', post_views.PostListAllView.as_view()),
    url('^post/create$', post_views.PostCreateView.as_view()),
]
