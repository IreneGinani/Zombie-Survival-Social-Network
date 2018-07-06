# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Survivor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    is_infected = models.BooleanField()
    count_reports = models.IntegerField()
    
    class Meta:
        verbose_name = u'Survivor'
        verbose_name_plural = u'Survivors'
        
    def __str__(self):
        return self.name
  
  
