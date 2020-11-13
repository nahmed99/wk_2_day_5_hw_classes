import unittest
from src.room import Room
from src.guest import Guest


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Cover Your Ears!", 15)
        self.guest = Guest("Sid The Sloth", 33)

    
    def test_room_has_name(self):
        self.assertEqual("Cover Your Ears!", self.room.name)

    
    def test_room_has_capacity(self):
        self.assertEqual(15, self.room.capacity)


    def test_room_start_at_0(self):
        self.assertEqual(0, self.room.guest_count())


    def test_song_start_at_0(self):
        self.assertEqual(0, self.room.song_count())


    def test_can_check_in_guest(self):
        self.room.check_in(self.guest)
        self.assertEqual(1, self.room.guest_count())