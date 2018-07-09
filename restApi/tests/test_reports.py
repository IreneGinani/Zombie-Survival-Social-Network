from django.test import TestCase
from model_mommy import mommy
from restApi.models import Survivor, Item, Inventory, Inventory_Items
from rest_framework.test import APITestCase
import json

class TestReports(APITestCase):

    fixtures = ['restApi/fixture/default.json']

    def test_noinfectedSurvivors(self):
        survivor1 = self.client.post('http://localhost:8000/api/v1/survivor/', {
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
                                                    "name": "Mario Fernandes",
                                                    "age": 30,
                                                    "gender": "M",
                                                    "latitude": -16.346867430274,
                                                    "longitude": -48.948227763174,
                                                    "is_infected": True,
                                                    "count_reports":0,
                                                    "inventory": {
  		                                                            "inventory_items": [
	  	                                                            {"id": 1 },
		                                                            {"id": 3 }
		                                                            ]
                                                                }
                                                    }, format='json')
        request = self.client.get('http://localhost:8000/api/v1/survivor/survivors_no_infected/')

        self.assertEquals(json.loads(request.content)['Percentage of no infected persons'],50)
        self.assertEquals(request.status_code, 200)

    def test_infectedSurvivors(self):
        survivor1 = self.client.post('http://localhost:8000/api/v1/survivor/', {
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
                                                    "name": "Mario Fernandes",
                                                    "age": 30,
                                                    "gender": "M",
                                                    "latitude": -16.346867430274,
                                                    "longitude": -48.948227763174,
                                                    "is_infected": True,
                                                    "count_reports":0,
                                                    "inventory": {
  		                                                            "inventory_items": [
	  	                                                            {"id": 1 },
		                                                            {"id": 3 }
		                                                            ]
                                                                }
                                                    }, format='json')
        request = self.client.get('http://localhost:8000/api/v1/survivor/survivors_infected/')

        self.assertEquals(json.loads(request.content)['Percentage of infected persons'],50)
        self.assertEquals(request.status_code, 200)

    def test_avgitems(self):
        survivor1 = self.client.post('http://localhost:8000/api/v1/survivor/', {
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
                                                    "name": "Mario Fernandes",
                                                    "age": 30,
                                                    "gender": "M",
                                                    "latitude": -16.346867430274,
                                                    "longitude": -48.948227763174,
                                                    "is_infected": False,
                                                    "count_reports":0,
                                                    "inventory": {
  		                                                            "inventory_items": [
	  	                                                            {"id": 2 },
		                                                            {"id": 4 }
		                                                            ]
                                                                }
                                                    }, format='json')
        request = self.client.get('http://localhost:8000/api/v1/survivor/avg_items/')

        self.assertEquals(json.loads(request.content)['Percentage of items per survivor']['water'],0.5)
        self.assertEquals(json.loads(request.content)['Percentage of items per survivor']['food'],0.5)
        self.assertEquals(json.loads(request.content)['Percentage of items per survivor']['ammunition'],0.5)
        self.assertEquals(json.loads(request.content)['Percentage of items per survivor']['medication'],0.5)
        self.assertEquals(request.status_code, 200)

    def test_pointslost_total(self):
        survivor1 = self.client.post('http://localhost:8000/api/v1/survivor/', {
                                                    "name": "Mario Fernandes",
                                                    "age": 30,
                                                    "gender": "M",
                                                    "latitude": -16.346867430274,
                                                    "longitude": -48.948227763174,
                                                    "is_infected": True,
                                                    "count_reports":0,
                                                    "inventory": {
  		                                                            "inventory_items": [
	  	                                                            {"id": 1 },
		                                                            {"id": 3 }
		                                                            ]
                                                                }
                                                    }, format='json')
        survivor2 = self.client.post('http://localhost:8000/api/v1/survivor/', {
                                                    "name": "Mario Fernandes",
                                                    "age": 30,
                                                    "gender": "M",
                                                    "latitude": -16.346867430274,
                                                    "longitude": -48.948227763174,
                                                    "is_infected": True,
                                                    "count_reports":0,
                                                    "inventory": {
  		                                                            "inventory_items": [
	  	                                                            {"id": 2 },
		                                                            {"id": 4 }
		                                                            ]
                                                                }
                                                    }, format='json')
        request = self.client.get('http://localhost:8000/api/v1/survivor/points_lost/')

        self.assertEquals(json.loads(request.content)['Total lost points'],10)
        self.assertEquals(request.status_code, 200)

    def test_pointslost_perperson(self):
        survivor1 = self.client.post('http://localhost:8000/api/v1/survivor/', {
                                                    "name": "Mario Fernandes",
                                                    "age": 30,
                                                    "gender": "M",
                                                    "latitude": -16.346867430274,
                                                    "longitude": -48.948227763174,
                                                    "is_infected": True,
                                                    "count_reports":0,
                                                    "inventory": {
  		                                                            "inventory_items": [
	  	                                                            {"id": 1 },
		                                                            {"id": 3 }
		                                                            ]
                                                                }
                                                    }, format='json')
        survivor2 = self.client.post('http://localhost:8000/api/v1/survivor/', {
                                                    "name": "Mario Fernandes",
                                                    "age": 30,
                                                    "gender": "M",
                                                    "latitude": -16.346867430274,
                                                    "longitude": -48.948227763174,
                                                    "is_infected": True,
                                                    "count_reports":0,
                                                    "inventory": {
  		                                                            "inventory_items": [
	  	                                                            {"id": 2 },
		                                                            {"id": 4 }
		                                                            ]
                                                                }
                                                    }, format='json')
        request = self.client.get('http://localhost:8000/api/v1/survivor/points_lost/1/')

        self.assertEquals(json.loads(request.content)['Total lost points from this survivor'],5)
        self.assertEquals(request.status_code, 200)    