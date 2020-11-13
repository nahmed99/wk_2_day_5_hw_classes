import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Roger Rabbit",25.90)

    
    def test_guest_has_name(self):
        self.assertEqual("Roger Rabbit", self.guest.name)

    
    def test_guest_has_money(self):
        self.assertEqual(25.90, self.guest.money)