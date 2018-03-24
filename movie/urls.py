from django.conf.urls import *
from rest_framework import routers
from movie import views

#       URL EXAMPLES
#       -       http://127.0.0.1:8000/movie/movie displays the ANGULAR PAGE but NO Data currently
#       -       http://127.0.0.1:8000/movie/movie#/movie/2 WILL talks to REST FRAMEWORK and retrieve details of move with movieID of 2
#       -

router = routers.DefaultRouter()
router.register(r'movie',views.MovieViewSet)    #       Routes to an angular page

urlpatterns = [
        url(r'^movie$',views.index),    #       Uses Django
        url(r'^api/',include(router.urls)),     #
]