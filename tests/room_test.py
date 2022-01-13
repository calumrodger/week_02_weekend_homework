import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
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

    def test_room_has_name(self):
        self.assertEqual("Room 213", self.room_1.name)

    def test_room_has_capacity(self):
        self.assertEqual(5, self.room_1.capacity)

    def test_guest_checks_in(self):
        self.room_1.guest_checks_in(self.guest_1)
        self.assertEqual(1, len(self.room_1.current_guests))
        self.assertEqual(10, self.guest_1.wallet)

    def test_guest_checks_out(self):
        self.room_1.guest_checks_in(self.guest_1)
        self.room_1.guest_checks_out(self.guest_1)
        self.assertEqual(0, len(self.room_1.current_guests))

    def test_add_song(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual(1, len(self.room_1.song_list))

    def test_room_too_full(self):
        self.room_2.guest_checks_in(self.guest_1)
        self.room_2.guest_checks_in(self.guest_2)
        self.assertEqual("not tonight pal", self.room_2.guest_checks_in(self.guest_3))