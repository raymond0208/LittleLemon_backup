from django.test import TestCase
#import unittest
from .models import Menu

# class MenuTest(TestCase):
#     def test_get_item(self):
#         item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
#         self.assertEqual(item, "IceCream : 80")
# #      #def test_get_item(self):
# #         #item = Menu.objects.create(Title="IceCream", Price=80.00, Inventory=100)
# #         #  self.assertEqual(item, 'IceCream: 80.00')
# #         # item = Menu.objects.object(1)
# #         # self.assertIsInstance(item.Inventory, int)

# def add(a,b):
#     return a + b

# class AddTest(unittest.TestCase):
#     def test_init(self):
#         self.assertEqual(add(1,2),3)
        
#     def test_err(self):
#         self.assertEqual(add(3,5),8.0)
        
# if __name__ == '__main__':
#     unittest.main()

class simpleTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title='IceCream', Price=80, Inventory=100)
        
    def test_model_add(self):
        item = Menu.objects.get(Title='IceCream')
        self.assertEqual(item.Price, 80)