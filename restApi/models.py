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
    count_reports = models.IntegerField(default = 0)

    
    class Meta:
        verbose_name = u'Survivor'
        verbose_name_plural = u'Survivors'
        
    def __str__(self):
        return self.name
  
class Item(models.Model):
    name = models.CharField(max_length=100)
    point = models.IntegerField()

    class Meta:
        verbose_name = u'Item'
        verbose_name_plural = u'Items'
        
    def __str__(self):
        return self.name

class Inventory(models.Model):

    survivor = models.OneToOneField(Survivor, verbose_name='Survivor')

    class Meta:
        verbose_name = u'Inventory'
        verbose_name_plural = u'Inventories'

class Inventory_Items(models.Model):

    inventories = models.ManyToManyField(Inventory, verbose_name='Inventories')
    items = models.IntegerField()

    class Meta:
        verbose_name = u'Inventory_Item'
        verbose_name_plural = u'Inventories_Items'


