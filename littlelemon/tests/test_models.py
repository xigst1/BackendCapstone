from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTest(TestCase):
    # @classmethod
    def test_get_item(self):
        item = Menu.objects.create(Title='IceCream', Price=80, Inventory=100)
        itemStr = item.get_item()
        self.assertEqual(itemStr, 'IceCream : 80', msg='pass')
        