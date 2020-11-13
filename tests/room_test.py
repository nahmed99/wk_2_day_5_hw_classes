import unittest
from src.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Cover Your Ears!", 15)

    
    def test_guest_has_name(self):
        self.assertEqual("Cover Your Ears!", self.room.name)

    
    def test_guest_has_age(self):
        self.assertEqual(15, self.room.capacity)