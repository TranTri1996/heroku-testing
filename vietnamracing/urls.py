from django.contrib import admin
from rest_framework import routers
from django.conf.urls import url
from racing import views

router = routers.DefaultRouter()

urlpatterns = [
    url('', views.index, name="index"),
    url('racing/', views.getAllRacing.as_view()),
    url('admin/', admin.site.urls),
]
