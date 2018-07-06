# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from restApi.models import Survivor
from restApi.serializers import SurvivorSerializer

@csrf_exempt
def survivor_list(request):
    """
    List all code survivors, or create a new snippet.
    """
    if request.method == 'GET':
        survivor = Survivor.objects.all()
        serializer = SurvivorSerializer(survivor, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Survivor_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)