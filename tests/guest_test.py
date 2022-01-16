import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.drink import Drink

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Heineken", 2)
        self.drink_2 = Drink("Double Voddy", 3)
        self.drink_3 = Drink("Shochu", 3)
        self.room_1 = Room("Room 213", 5, 0, 5, True)
        self.room_2 = Room("Cosy Corner", 2, 0, 10, False)
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
        

    def test_guest_has_name(self):
        self.assertEqual("Timmy", self.guest_1.name)

    def test_guest_has_wallet(self):
        self.assertEqual(20, self.guest_1.wallet)
 
    def test_pay_entry(self):
        self.guest_1.pay_entry(self.room_1)
        self.assertEqual(15, self.guest_1.wallet)

    def test_pay_entry_2(self):
        self.guest_6.pay_entry(self.room_1)
        self.assertEqual("not tonight pal", self.guest_6.pay_entry(self.room_1))

    def test_guest_fav_song_is_on_list(self):
        self.room_1.add_song(self.song_1)
        self.room_1.add_song(self.song_2)
        self.room_1.guest_checks_in(self.guest_1, self.room_1)
        self.assertEqual(2, len(self.room_1.song_list))
        self.assertEqual("woot woot", self.guest_1.guest_fav_song_is_on_list(self.room_1))

    def test_buy_drink(self):
        self.room_1.add_drink(self.drink_1)
        self.room_1.add_drink(self.drink_2)
        self.guest_1.buy_drink(self.drink_1, self.room_1)
        self.assertEqual(18, self.guest_1.wallet)
        self.assertEqual(2, self.room_1.tab)




