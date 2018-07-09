from django.test import TestCase
from model_mommy import mommy
from django.utils.timezone import datetime
from restApi.models import Survivor, Item, Inventory, Inventory_Items
from rest_framework.test import APITestCase
import json

class TestSurvivorCreation(APITestCase):

    fixtures = ['restApi/fixture/default.json']
  
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
        
    def test_survivor_trade_notfound_survivor(self):

        resques_notfound = self.client.put('http://localhost:8000/api/v1/survivor/trade_items/1/1-food/2/3-food/')
        self.assertEquals(resques_notfound.status_code, 404)

    def test_survivor_trade_amountdontmatch(self):
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
        survivor1 = self.client.post('http://localhost:8000/api/v1/survivor/', {
                                                    "name": "Maria Aparecida",
                                                    "age": 30,
                                                    "gender": "F",
                                                    "latitude": 10.0909,
                                                    "longitude": 8.45,
                                                    "is_infected": False,
                                                    "count_reports":0,
                                                    "inventory": {
  		                                                            "inventory_items": [
	  	                                                            {"id": 1 },
		                                                            {"id": 2 }
		                                                            ]
                                                                }
                                                    }, format='json')

        request_amounterror = self.client.put('http://localhost:8000/api/v1/survivor/trade_items/1/4-food/2/3-food/')
        self.assertEquals(request_amounterror.status_code, 400)
        self.assertEquals(json.loads(request_amounterror.content)['error'], "Amount don't match")

    def test_survivor_trade_itemnotfound(self):

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
        survivor1 = self.client.post('http://localhost:8000/api/v1/survivor/', {
                                                    "name": "Maria Aparecida",
                                                    "age": 30,
                                                    "gender": "F",
                                                    "latitude": 10.0909,
                                                    "longitude": 8.45,
                                                    "is_infected": False,
                                                    "count_reports":0,
                                                    "inventory": {
  		                                                            "inventory_items": [
	  	                                                            {"id": 1 },
		                                                            {"id": 2 }
		                                                            ]
                                                                }
                                                    }, format='json')

        request_itemerror = self.client.put('http://localhost:8000/api/v1/survivor/trade_items/1/1-food/2/1-juice/')
       
        self.assertEquals(request_itemerror.status_code, 404)
        self.assertEquals(json.loads(request_itemerror.content)['error'], "Item does not exists")

    def test_survivor_trade_pointsdontmatch(self):
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
        survivor1 = self.client.post('http://localhost:8000/api/v1/survivor/', {
                                                    "name": "Maria Aparecida",
                                                    "age": 30,
                                                    "gender": "F",
                                                    "latitude": 10.0909,
                                                    "longitude": 8.45,
                                                    "is_infected": False,
                                                    "count_reports":0,
                                                    "inventory": {
  		                                                            "inventory_items": [
	  	                                                            {"id": 1 },
		                                                            {"id": 2 }
		                                                            ]
                                                                }
                                                    }, format='json')

        request_pointserror = self.client.put('http://localhost:8000/api/v1/survivor/trade_items/1/1-food/2/1-water/')
       
        self.assertEquals(request_pointserror.status_code, 400)
        self.assertEquals(json.loads(request_pointserror.content)['error'], "Points don't match")
        
    def test_survivor_trade_survivorinfected(self):

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

        survivor2 = self.client.post('http://localhost:8000/api/v1/survivor/', {
                                                    "name": "Maria Aparecida",
                                                    "age": 30,
                                                    "gender": "F",
                                                    "latitude": 10.0909,
                                                    "longitude": 8.45,
                                                    "is_infected": True,
                                                    "count_reports":0,
                                                    "inventory": {
  		                                                            "inventory_items": [
	  	                                                            {"id": 1 },
		                                                            {"id": 2 }
		                                                            ]
                                                                }
                                                    }, format='json')

        request_infectionserror = self.client.put('http://localhost:8000/api/v1/survivor/trade_items/1/1-food/2/1-food/')
       
        self.assertEquals(request_infectionserror.status_code, 400)
        self.assertEquals(json.loads(request_infectionserror.content)['error'], "Survivor is infected")
        