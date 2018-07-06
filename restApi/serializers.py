from rest_framework import serializers
from .models import Survivor


class SurvivorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return  Survivor.objects.create(**validated_data)
    
    def update(self, validated_data):
        instance.title = validated_data.get('longitude', instance.longitude)
        instance.save()
        return instance