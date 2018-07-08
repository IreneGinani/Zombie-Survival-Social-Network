from rest_framework import serializers
from .models import Survivor, Inventory, Inventory_Items, Item


class SurvivorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survivor
        fields = ('id','name', 'age', 'gender', 'longitude', 'latitude', 'is_infected')

class Survivor_LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survivor
        fields = ('longitude', 'latitude')

class InventorySerializer(serializers.ModelSerializer):
    """
    A inventory serializer to return the inventory details
    """
    survivor = SurvivorSerializer(required=True)

    class Meta:
        model = Inventory
        fields = ('survivor',)

class Inventory_ItemsSerializer(serializers.ModelSerializer):
    """
    A inventory_item serializer to return the items in inventory
    """
    inventories = InventorySerializer(read_only=True,many=True)

    class Meta:
        model = Inventory_Items
        fields = ('inventories', 'items', 'survivor_id')

