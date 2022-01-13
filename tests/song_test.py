import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Room 213", 5)
        self.room_2 = Room("Cosy Corner", 2)
        self.guest_1 = Guest("Timmy", 20)
        self.guest_2 = Guest("Jane", 20)
        self.guest_3 = Guest("Bob", 20)
        self.guest_4 = Guest("Tom", 20)
        self.guest_5 = Guest("Ephesia", 100)
        self.guest_6 = Guest("Norbert", 9)
        self.song_1 = Song("Walking on Sunshine")
        self.song_2 = Song("Song 2")
        self.song_3 = Song("4:33")
        self.song_4 = Song("Everyone's Free to Wear Sunscreen")

    def test_song_has_name(self):
        self.assertEqual("Walking on Sunshine", self.song_1.name)
