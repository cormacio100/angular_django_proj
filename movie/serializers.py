from rest_framework import serializers
from .models import Movie
from django.contrib.auth.models import User

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        #   fields to expose
        fields = ('title','id','genre')

