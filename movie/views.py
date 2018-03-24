# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Movie
from .permissions import IsOwnerOrReadOnly


"""
    EXAMPLE URL
    http://127.0.0.1:8000/movie/api/movie/3/
    Made up of:
    HOST/APP/URL/OBJECT/OBJECT_ID
"""

def index(request):
    return render_to_response('movie/movie.html')#,RequestContext(request))



# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    #   add a permission
    #   Only a superuser can edit
    permission_class = (IsOwnerOrReadOnly,)

    #   override the save method
    def pre_save(self,obj):
        #   set the current user as the owner of the Movie_old object
        #   This insures that only they will be able to edit
        #   movies that are added (on the same login)
        obj.owner = self.request.user
