import unittest
from src.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Bad", "You're a very naughty boy. Now go away.")

    
    def test_song_has_name(self):
        self.assertEqual("Bad", self.song.name)


    def test_song_has_lyrics(self):
        self.assertEqual("You're a very naughty boy. Now go away.", self.song.lyrics)