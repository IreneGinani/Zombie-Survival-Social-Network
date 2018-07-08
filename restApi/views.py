# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from restApi.models import Survivor, Inventory_Items
from restApi.serializers import SurvivorSerializer, InventorySerializer, Inventory_ItemsSerializer
from restApi.serializers import Survivor_LocationSerializer

@csrf_exempt
def survivor_create(request):
    """
    List all code survivors, or create a new survivor.
    """
    if request.method == 'GET':
        survivor = Survivor.objects.all()
        serializer = SurvivorSerializer(survivor, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        name = data['name']
        age = data['age']
        gender = data['gender']
        latitude = data['latitude']
        longitude = data['longitude']
        is_infected = data['is_infected']
        if (is_infected == False):
            is_infected = False
        else:
            is_infected = True
        survivor_s = Survivor(name, age, gender, longitude, latitude,is_infected)
        dic_survivor = { "survivor": {
                             'name': name,
                             'age' : int(age),
                             'gender': gender,
                             'longitude': float(longitude),
                             'latitude': float(latitude),
                             'is_infected': is_infected
                }
        }
        
        survivor_serializer = SurvivorSerializer(data=data)
        inventory_serializer = InventorySerializer(data=dic_survivor)
               
        try:
            if survivor_serializer.is_valid():
                s = survivor_serializer.save()
            inventory_items = data['inventory']['inventory_items']
            if inventory_serializer.is_valid():
                for element in inventory_items:
                   
                    dic_inventory = { "survivor_id": s.id, "items": int(element['id']), "inventories": 
                                        [{'survivor': {
                                                       'name': name,
                                                       'age' : int(age),
                                                       'gender': gender,
                                                       'longitude': float(longitude),
                                                       'latitude': float(latitude),
                                                       'is_infected': is_infected
                                                    }
                                        },
                                        ]
                    }
                    print(dic_inventory)
                    inventory_items_serializer = Inventory_ItemsSerializer(data=dic_inventory)
                    if inventory_items_serializer.is_valid():
                        inventory_items_serializer.save()
                return JsonResponse(inventory_items_serializer.data, status=200)
                inventory_serializer.save()
        except KeyError:
            print ("Inventory is Requerid")

@csrf_exempt
def survivor_update(request, pk):
    """
    Retrieve, update or delete a code survivor.
    """
    try:
        survivor = Survivor.objects.get(pk=pk)
    except Survivor.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Survivor_LocationSerializer(survivor, data=data)
        if serializer.is_valid():
            serializer.save()
            s_serializer = SurvivorSerializer(survivor)
            return JsonResponse(s_serializer.data)
        return JsonResponse(serializer.errors, status=400)

def inventories_items(request):
    if request.method == 'GET':
        inventories_items = Inventory_Items.objects.all()
        serializer = Inventory_ItemsSerializer(inventories_items, many=True)
        return JsonResponse(serializer.data, safe=False)
