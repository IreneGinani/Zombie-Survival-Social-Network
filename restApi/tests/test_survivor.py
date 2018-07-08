from django.test import TestCase
from model_mommy import mommy
from django.utils.timezone import datetime
from restApi.models import Survivor, Item, Inventory, Inventory_Items
from rest_framework.test import APIRequestFactory

class TestSurvivorCreation(TestCase):
  
    def test_survivor_creation(self):
        factory = APIRequestFactory()
        request = factory.post('api/v1/survivor/', {
                                                    "name": "Mario Fernandes",
                                                    "age": 30,
                                                    "gender": "M",
                                                    "latitude": -16.346867430274,
                                                    "longitude": -48.948227763174,
                                                    "is_infected": False,
                                                    "count_reports":0,
                                                    "inventory": {
  		                                                            "inventory_items": [
	  	                                                            {"id": 1 },
		                                                            {"id": 3 }
		                                                            ]
                                                                }
                                                    }, format='json')
    def test_survivor_update_location(self):
        factory = APIRequestFactory()
        request = factory.post('api/v1/survivor/3', {
                                                    "latitude": -16.346867430274,
                                                    "longitude": -48.948227763174,
                                                    }, format='json')



        
        
