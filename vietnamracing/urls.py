from rest_framework import routers
from django.conf.urls import url, include

router = routers.DefaultRouter()

urlpatterns = [
    url('api/', include('racing.urls')),
]
