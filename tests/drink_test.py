import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Heineken", 2)
        self.drink_2 = Drink("Double Voddy", 3)
        self.drink_3 = Drink("Shochu", 3)
        self.room_1 = Room("Room 213", 5, 0)
        self.room_2 = Room("Cosy Corner", 2, 0)
        self.song_1 = Song("Walking on Sunshine")
        self.song_2 = Song("Song 2")
        self.song_3 = Song("4:33")
        self.song_4 = Song("Everyone's Free to Wear Sunscreen")
        self.guest_1 = Guest("Timmy", 20, self.song_2)
        self.guest_2 = Guest("Jane", 20, self.song_3)
        self.guest_3 = Guest("Bob", 20, self.song_1)
        self.guest_4 = Guest("Tom", 20, self.song_4)
        self.guest_5 = Guest("Ephesia", 100, self.song_3)
        self.guest_6 = Guest("Norbert", 9, self.song_4)
    
    def test_drink_has_name(self):
        self.assertEqual("Heineken", self.drink_1.name)
    
    def test_drink_has_price(self):
        self.assertEqual(2, self.drink_1.price)