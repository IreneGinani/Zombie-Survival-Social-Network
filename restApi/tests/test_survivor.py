from django.test import TestCase
from model_mommy import mommy
from django.utils.timezone import datetime
from restApi.models import Survivor, Item, Inventory, Inventory_Items
from rest_framework.test import APITestCase
import json

class TestSurvivorCreation(APITestCase):
  
    def test_survivor_creation(self):
        request = self.client.post('http://localhost:8000/api/v1/survivor/', {
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
        self.assertEquals(request.status_code, 200)
        
    def test_survivor_update_location(self):
        survivor = self.client.post('http://localhost:8000/api/v1/survivor/', {
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
        request = self.client.put('http://localhost:8000/api/v1/survivor/1/', {
                                                    "latitude": 10,
                                                    "longitude": -174,
                                                    }, format='json')
        self.assertEquals(request.status_code, 200)
        self.assertEquals(json.loads(request.content)['latitude'],10)
        self.assertEquals(json.loads(request.content)['longitude'],-174)
    
    def test_survivor_update_location404(self):
        request = self.client.put('http://localhost:8000/api/v1/survivor/1/', {
                                                    "latitude": -16.346867430274,
                                                    "longitude": -48.948227763174,
                                                    }, format='json')
        self.assertEquals(request.status_code, 404)
    
    def test_report_infection(self):
        survivor = self.client.post('http://localhost:8000/api/v1/survivor/', {
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
        request = self.client.put('http://localhost:8000/api/v1/survivor/report_infection/1/')
        self.assertEquals(request.status_code, 200)
        self.assertEquals(json.loads(request.content)['count_reports'], 1)
        self.assertEquals(json.loads(request.content)['is_infected'], False)

        request_2 = self.client.put('http://localhost:8000/api/v1/survivor/report_infection/1/')
        request_3 = self.client.put('http://localhost:8000/api/v1/survivor/report_infection/1/')

        self.assertEquals(json.loads(request_3.content)['is_infected'], True)
        
