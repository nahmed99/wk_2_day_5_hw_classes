import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Roger Rabbit", 57)

    
    def test_guest_has_name(self):
        self.assertEqual("Roger Rabbit", self.guest.name)

    
    def test_guest_has_age(self):
        self.assertEqual(57, self.guest.age)