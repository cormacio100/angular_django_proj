# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from star.models import Star
import datetime

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=128,null=False,blank=True,unique=True)
    theatreReleaseDate = models.DateField(null=True, blank=True)
    theatreRelease = models.TextField(max_length=380,null=True,blank=True)
    #image = models.TextField(max_length=500, null=True, blank=True)
    genre = models.TextField(max_length=100,null=True,blank=True)
    star = models.TextField(max_length=1000,null=True,blank=True)
    #stars = models.ManyToManyField(Star,blank=True,null=True)

    def get_absolut_yrl(self):
        return "/movie/%i/"% self.pk

    def __unicode__(self):
        return self.title