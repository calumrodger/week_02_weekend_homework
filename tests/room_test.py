import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.drink import Drink

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.drinks = (Drink("Heineken", 2), Drink("Double Voddy", 3))
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

    def test_room_has_name(self):
        self.assertEqual("Room 213", self.room_1.name)

    def test_room_has_capacity(self):
        self.assertEqual(5, self.room_1.capacity)

    def test_guest_checks_in(self):
        self.room_1.guest_checks_in(self.guest_1, self.room_1)
        # self.room_1.add_entry_fee_to_tab()
        self.assertEqual(1, len(self.room_1.current_guests))
        self.assertEqual(15, self.guest_1.wallet)
        self.assertEqual(5, self.room_1.tab)

    def test_guest_checks_out(self):
        self.room_1.guest_checks_in(self.guest_1, self.room_1)
        self.room_1.guest_checks_out(self.guest_1)
        self.assertEqual(0, len(self.room_1.current_guests))

    def test_add_song(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual(1, len(self.room_1.song_list))

    def test_room_too_full(self):
        self.room_2.guest_checks_in(self.guest_1, self.room_2)
        self.room_2.guest_checks_in(self.guest_2, self.room_2)
        self.assertEqual("not tonight pal", self.room_2.guest_checks_in(self.guest_3, self.room_2))

    def test_add_entry_fee_to_tab(self):
        self.room_1.add_entry_fee_to_tab()
        self.assertEqual(5, self.room_1.tab)

    def test_add_drink(self):
        self.room_1.add_drink(self.drink_1)
        self.assertEqual(1, len(self.room_1.drink_list))

# an alternative - make list of objects rather than create them individually
    def test_add_drink(self):
        self.room_1.add_drink(self.drinks[0])
        self.assertEqual(1, len(self.room_1.drink_list))

    def test_tab_accumulation(self):
        self.room_2.add_drink(self.drink_1)
        self.room_2.add_drink(self.drink_2)
        self.room_2.add_drink(self.drink_3)
        self.room_2.guest_checks_in(self.guest_1, self.room_2)
        self.room_2.guest_checks_in(self.guest_2, self.room_2)
        self.assertEqual(10, self.guest_1.wallet)
        self.assertEqual(10, self.guest_2.wallet)
        self.assertEqual(20, self.room_2.tab)
        self.guest_1.buy_drink(self.drink_1, self.room_2)
        self.guest_2.buy_drink(self.drink_2, self.room_2)
        self.assertEqual(8, self.guest_1.wallet)
        self.assertEqual(7, self.guest_2.wallet)
        self.assertEqual(25, self.room_2.tab)

    def test_has_tambourine(self):
        self.assertEqual("yes, it has a tambourine!!", self.room_1.has_tambourine())



