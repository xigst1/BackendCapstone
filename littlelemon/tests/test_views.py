from django.test import TestCase
from rest_framework.test import APIClient
# from restaurant.views import MenuItemView
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    
      
    def setup(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.item2 = Menu.objects.create(Title="Beer", Price=20, Inventory=20)
        
    def test_getall(self):
        request = self.client.get('/restaurant/menu/')
        testData = MenuSerializer(Menu.objects.all(), many=True)
        
        self.assertEqual(request.data, testData.data)        

    


