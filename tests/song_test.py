import unittest
from classes.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Bad")

    
    def test_song_has_name(self):
        self.assertEqual("Bad", self.song.name)