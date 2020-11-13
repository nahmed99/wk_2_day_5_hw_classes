import unittest
from classes.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Bad", "You're bad. Behave yourself.")

    
    def test_song_has_name(self):
        self.assertEqual("Bad", self.song.name)


    def test_song_has_lyrics(self):
        self.assertEqual("You're bad. Behave yourself.", self.song.lyrics)