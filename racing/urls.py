from rest_framework import routers
from django.conf.urls import url
from racing.views import biker_views, auth_views, product_views

router = routers.DefaultRouter()

urlpatterns = [
    url('^account/register$', auth_views.RegisterView.as_view()),
    url('^account/login$', auth_views.LoginView.as_view()),
    url('^account/logout$', auth_views.LogoutView.as_view()),
    url('^account/forgot_password$', auth_views.ForgotPasswordView.as_view()),
    url('^account/change_password$', auth_views.ChangePasswordView.as_view()),

    url('^biker/profile$', biker_views.BikerGetProfileView.as_view()),

    url('^product/create$', product_views.CreateProductView.as_view()),
    url('^product/list$', product_views.GetPersonalProductListView.as_view())
]
