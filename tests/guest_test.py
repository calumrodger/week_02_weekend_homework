import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
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

    def test_guest_has_name(self):
        self.assertEqual("Timmy", self.guest_1.name)

    def test_guest_has_wallet(self):
        self.assertEqual(20, self.guest_1.wallet)
 
    def test_pay_entry(self):
        self.guest_1.pay_entry()
        self.assertEqual(10, self.guest_1.wallet)

    def test_pay_entry_2(self):
        self.guest_6.pay_entry()
        self.assertEqual("not tonight pal", self.guest_6.pay_entry())




