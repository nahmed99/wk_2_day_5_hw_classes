import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Roger Rabbit",25.90, "Bad")

    
    def test_guest_has_name(self):
        self.assertEqual("Roger Rabbit", self.guest.name)

    
    def test_guest_has_money(self):
        self.assertEqual(25.90, self.guest.money)


    def test_guest_has_fav_song(self):
        self.assertEqual("Bad", self.guest.fav_song)