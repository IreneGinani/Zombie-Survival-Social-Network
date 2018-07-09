# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from restApi.models import Survivor, Inventory_Items, Item
from restApi.serializers import SurvivorSerializer, Inventory_ItemsSerializer
from restApi.serializers import Survivor_LocationSerializer, ItemSerializer

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
        count_reports = 0
        if (is_infected == False):
            is_infected = False
        else:
            is_infected = True

        survivor_serializer = SurvivorSerializer(data=data)
               
        try:
            if survivor_serializer.is_valid():
                
                s = survivor_serializer.save()
            inventory_items = data['inventory']['inventory_items']
            for element in inventory_items:
                   
                dic_inventory = { "survivor_id": s.id, "items": int(element['id']), "inventories": 
                                        [{'survivor': {
                                                       'name': name,
                                                       'age' : int(age),
                                                       'gender': gender,
                                                       'longitude': float(longitude),
                                                       'latitude': float(latitude),
                                                       'is_infected': is_infected,
                                                       'count_reports': count_reports
                                                    }
                                        },
                                        ]
                    }
                inventory_items_serializer = Inventory_ItemsSerializer(data=dic_inventory)
                if inventory_items_serializer.is_valid():
                    inventory_items_serializer.save()
            return JsonResponse(survivor_serializer.data, status=200)
        except KeyError:
            return HttpResponse(json.dumps({"error":"Inventory is Requerid"}), content_type="application/json", status=404)


@csrf_exempt
def survivor_update(request, pk):
    """
    Retrieve, update or delete a code survivor.
    """
    try:
        survivor = Survivor.objects.get(pk=pk)
    except Survivor.DoesNotExist:
        return HttpResponse(json.dumps({"error":"Survivor does not exists"}), content_type="application/json", status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Survivor_LocationSerializer(survivor, data=data)
        if serializer.is_valid():
            serializer.save()
            s_serializer = SurvivorSerializer(survivor)
            return JsonResponse(s_serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

def inventories_items(request):
    if request.method == 'GET':
        inventories_items = Inventory_Items.objects.all()
        serializer = Inventory_ItemsSerializer(inventories_items, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def report_infection(request, pk):
   
    try:
        survivor = Survivor.objects.get(pk=pk)
    except Survivor.DoesNotExist:
        return HttpResponse(json.dumps({"error":"Survivor does not exists"}), content_type="application/json", status=404)
    count_reports = survivor.count_reports + 1

    if count_reports == 3:
        data =  {
        "name": survivor.name,
        "age": survivor.age,
        "gender": survivor.gender,
        "longitude": survivor.longitude,
        "latitude": survivor.latitude,
        "is_infected": True,
        "count_reports": count_reports
        }
    else:
        data =  {
        "name": survivor.name,
        "age": survivor.age,
        "gender": survivor.gender,
        "longitude": survivor.longitude,
        "latitude": survivor.latitude,
        "is_infected": survivor.is_infected,
        "count_reports": count_reports
    }

    if request.method == 'PUT':
        survivor_serializer = SurvivorSerializer(survivor,data=data)
        if survivor_serializer.is_valid():
            survivor_serializer.save()
            s_serializer = SurvivorSerializer(survivor)
            return JsonResponse(s_serializer.data, status=200)
        return JsonResponse(s_serializer.errors, status=400)

@csrf_exempt
def trade_items(request, pk, slug, month, username):

    pk_1 = pk
    items_1 = slug
    pk_2 = month
    items_2 = username
    dic_items1 = {}
    dic_items2 = {}
    soma_total1 = 0
    soma_total2 = 0
    
    if request.method == 'PUT':
        try:
            survivor_1 = Survivor.objects.get(pk=pk_1)
            survivor_2 = Survivor.objects.get(pk=pk_2)
        except Survivor.DoesNotExist:
            return HttpResponse(json.dumps({"error":"Survivor does not exists"}), content_type="application/json", status=404)

        try:
            inventory_1 = Inventory_Items.objects.filter(survivor_id=pk_1)
            inventory_2 = Inventory_Items.objects.filter(survivor_id=pk_2)
        except Inventory_Items.DoesNotExist:
            return HttpResponse(json.dumps({"error":"Inventory does not exists"}), content_type="application/json", status=404)
        

        types_items1 = items_1.split("-")
        types_items2 = items_2.split("-")


        for i in xrange(0, len(types_items1)):
            if(i%2 == 0):
                try:
                    item = Item.objects.get(name=types_items1[i+1])
                    dic_items1[types_items1[i+1]] = int(types_items1[i])
                    items1 = Item.objects.filter(name=types_items1[i+1])
                    if (items1.count() != int(types_items1[i])):
                        return HttpResponse(json.dumps({"error":"Amount don't match"}), content_type="application/json", status=400)
                except Item.DoesNotExist:
                    return HttpResponse(json.dumps({"error":"Item does not exists"}), content_type="application/json", status=404)
                
                iv = Inventory_Items.objects.filter(items=item.pk,survivor_id=survivor_1.id)
                if (iv.count() == 0):
                    return HttpResponse(json.dumps({"error":"Item in inventory does not exists"}), content_type="application/json", status=404)
                
                soma_total1 += int(types_items1[i])*item.point

        for i in xrange(0, len(types_items2)):
            if(i%2 == 0):
                try:
                    item = Item.objects.get(name=types_items2[i+1])
                    items2 = Item.objects.filter(name=types_items2[i+1])
                    dic_items2[types_items2[i+1]] = int(types_items2[i])
                    if (items2.count() != int(types_items2[i])):
                        return HttpResponse(json.dumps({"error":"Amount don't match"}), content_type="application/json", status=400)
                except Item.DoesNotExist:
                    return HttpResponse(json.dumps({"error":"Item does not exists"}), content_type="application/json", status=404)
              
                iv = Inventory_Items.objects.filter(items=item.pk,survivor_id=survivor_2.id)
                if (iv.count() == 0):
                    return HttpResponse(json.dumps({"error":"Item in inventory does not exists"}), content_type="application/json", status=404)
                
                soma_total2 += int(types_items2[i])*item.point
       
        if (soma_total1 != soma_total2):
            return HttpResponse(json.dumps({"error":"Points don't match"}), content_type="application/json", status=400)

        elif(survivor_1.is_infected) or (survivor_2.is_infected):
            return HttpResponse(json.dumps({"error":"Survivor is infected"}), content_type="application/json", status=400)

        else:
            for key in dic_items1:
                items1 = Item.objects.get(name=key)
                dic_inventory = { "survivor_id": pk_2, "items": items1.pk, "inventories": 
                                        [{'survivor': {
                                                       'name': survivor_2.name,
                                                       'age' : survivor_2.age,
                                                       'gender': survivor_2.gender,
                                                       'longitude': survivor_2.longitude,
                                                       'latitude': survivor_2.latitude,
                                                       'is_infected': survivor_2.is_infected,
                                                       'count_reports': 0
                                                    }
                                        },
                                        ]
                    }
                inventory_items_serializer = Inventory_ItemsSerializer(data=dic_inventory)
                if inventory_items_serializer.is_valid():
                    inventory_items_serializer.save()
                Inventory_Items.objects.filter(survivor_id=pk_1,items=items1.pk).first().delete()
                
            for key in dic_items2:
                items2 = Item.objects.get(name=key)
                dic_inventory = { "survivor_id": pk_1, "items": items2.pk, "inventories": 
                                        [{'survivor': {
                                                       'name': survivor_1.name,
                                                       'age' : survivor_1.age,
                                                       'gender': survivor_1.gender,
                                                       'longitude': survivor_1.longitude,
                                                       'latitude': survivor_1.latitude,
                                                       'is_infected': survivor_1.is_infected,
                                                       'count_reports': 0
                                                    }
                                        },
                                        ]
                    }
                inventory_items_serializer = Inventory_ItemsSerializer(data=dic_inventory)
                if inventory_items_serializer.is_valid():
                    inventory_items_serializer.save()
                Inventory_Items.objects.filter(survivor_id=pk_2,items=items2.pk).first().delete()
            return HttpResponse(json.dumps({"Success":"Exchange made successfully"}), content_type="application/json", status=200)

    return HttpResponse(json.dumps({"error":"Verify the method in request"}), content_type="application/json", status=200)

def infected_survivors_report(request):
    infected = 0.0

    if request.method == 'GET':
        survivor = Survivor.objects.all()
        for s in survivor:
            if s.is_infected:
                infected+=1

        porcent_infected = (infected/survivor.count())*100
        return HttpResponse(json.dumps({"Percentage of infected persons": porcent_infected}), content_type="application/json", status=200)

def no_infected_survivors_report(request):
    no_infected = 0.0

    if request.method == 'GET':
        survivor = Survivor.objects.all()
        for s in survivor:
            if not(s.is_infected):
                no_infected+=1

        porcent_no_infected = (no_infected/survivor.count())*100
        return HttpResponse(json.dumps({"Percentage of no infected persons": porcent_no_infected}), content_type="application/json", status=200)

def avg_items(request):

    sum_water = 0.0
    sum_food = 0.0
    sum_ammunition = 0.0
    sum_medication = 0.0

    if request.method == 'GET':
        inventories = Inventory_Items.objects.all()
        survivors = Survivor.objects.all()
        for i in inventories:

            survivor = Survivor.objects.get(pk=i.survivor_id)

            if not(survivor.is_infected):

                if i.items == 1:
                    sum_food +=1
                elif i.items == 2:
                    sum_water+=1
                elif i.items == 3:
                    sum_medication+=1
                elif i.items == 4:
                    sum_ammunition+=1
        
        avg_food = sum_food/survivors.count()
        avg_water = sum_water/survivors.count()
        avg_ammunition = sum_ammunition/survivors.count()
        avg_medication = sum_medication/survivors.count()

        return HttpResponse(json.dumps({"Percentage of items per survivor": {"ammunition": avg_ammunition, "medication": avg_medication, "food":avg_food, "water":avg_water }}), content_type="application/json", status=200)

def points_lost(request):

    points_lost = 0

    if request.method == 'GET':
        survivors = Survivor.objects.all()

        for survivor in survivors:
            if survivor.is_infected:
                inventories = Inventory_Items.objects.filter(survivor_id=survivor.id)
                for i in inventories:
                    item = Item.objects.get(pk=i.items)
                    points_lost += item.point
       
        return HttpResponse(json.dumps({"Total lost points": points_lost}), content_type="application/json", status=200)

def points_lost_survivor(request,pk):

    points_lost = 0

    if request.method == 'GET':
        try:
            survivor = Survivor.objects.get(pk=pk)
        except Survivor.DoesNotExist:
            return HttpResponse(json.dumps({"error":"Survivor does not exists"}), content_type="application/json", status=404)

        if survivor.is_infected:
            inventories = Inventory_Items.objects.filter(survivor_id=survivor.id)
            for i in inventories:
                item = Item.objects.get(pk=i.items)
                points_lost += item.point
        else:
            return HttpResponse(json.dumps({"error":"This survivor are not infected"}), content_type="application/json", status=404)

       
        return HttpResponse(json.dumps({"Total lost points from this survivor": points_lost}), content_type="application/json", status=200)
