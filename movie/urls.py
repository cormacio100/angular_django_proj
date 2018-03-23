from django.conf.urls import *
from rest_framework import routers
from movie import views

router = routers.DefaultRouter()
router.register(r'movie',views.MovieViewSet)

urlpatterns = [
        url(r'^movie$',views.index),
        url(r'^api/',include(router.urls)),
]