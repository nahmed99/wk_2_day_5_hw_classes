import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Cover Your Ears!", 15)
        self.guest = Guest("Sid The Sloth", 33)
        self.song = Song("Ask me if I'm a pineapple", "Are you a pineapple? No.")

    
    def test_room_has_name(self):
        self.assertEqual("Cover Your Ears!", self.room.name)

    
    def test_room_has_capacity(self):
        self.assertEqual(15, self.room.capacity)


    def test_room_start_at_0(self):
        self.assertEqual(0, self.room.guest_count())


    def test_can_check_in_guest(self):
        self.room.check_in(self.guest)
        self.assertEqual(1, self.room.guest_count())


    def test_can_find_guess_by_name(self):
        # Add guest to room
        self.room.check_in(self.guest)

        # 'Extract' guest object from room, using their name
        guest = self.room.check_out("Sid The Sloth")
        self.assertEqual("Sid The Sloth", guest.name)

    
    def test_song_start_at_0(self):
        self.assertEqual(0, self.room.song_count())


    def test_can_add_song(self):
        self.room.add_song(self.song)
        self.assertEqual(1, self.room.song_count())
