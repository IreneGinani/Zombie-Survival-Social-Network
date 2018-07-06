from django.test import TestCase
from model_mommy import mommy
from django.utils.timezone import datetime
from resApi.models import Survivor, Item, Inventory, Inventory_Items

class TestSurvivor(TestCase):
  
  def setUp(self):
    self.survivor = mommy.make(Survivor, name='Irene')
      
  def test_record_creation(self):
    self.assertTrue(isinstance(self.survivor, Survivor))
    self.assertEquals(self.survivor.__str__(), self.survivor.name)