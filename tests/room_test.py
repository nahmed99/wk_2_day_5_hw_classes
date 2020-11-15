import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Cover Your Ears!", 15, 10)
        self.room_small = Room("Tight Squeeze", 1, 15)
        self.guest = Guest("Sid The Sloth", 33.25)
        self.guest_no_money = Guest("Scrooge", 3.99)
        self.song = Song("Hold a chicken in the air")

    
    def test_room_has_name(self):
        self.assertEqual("Cover Your Ears!", self.room.name)

    
    def test_room_has_capacity(self):
        self.assertEqual(15, self.room.capacity)


    def test_room_has_entry_fee(self):
        self.assertEqual(10, self.room.entry_fee)


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


    def test_capacity_for_more_guests(self):
        self.assertEqual(True, self.room.check_capacity())


    def test_capacity_no_more_guests(self):
        self.room_small.check_in(self.guest)
        self.assertEqual(False, self.room_small.check_capacity())


    def test_guest_has_funds(self):
        self.assertEqual(True, self.room_small.confirm_guest_has_funds(self.guest))


    def test_guest_has_not_funds(self):
        self.assertEqual(False, self.room.confirm_guest_has_funds(self.guest_no_money))


    def test_take_fee_from_guest(self):
        # Take fee from the guest
        self.room.take_fee_from_guest(self.guest)

        # The guest should now have 10 less than before
        self.assertEqual(23.25, self.guest.money)


    def test_take_no_fee_from_guest(self):
        # Try to take fee from the guest - this ones doesn't have sufficient funds
        self.room_small.take_fee_from_guest(self.guest_no_money)

        # The guest should still have the same amount of money as before.
        self.assertEqual(3.99, self.guest_no_money.money)
        