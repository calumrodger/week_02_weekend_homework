class Room:

    def __init__(self, name, capacity, tab, entry_fee, tambourine):
        self.name = name
        self.capacity = capacity
        self.current_guests = []
        self.song_list = []
        self.tab = tab
        self.drink_list = []
        self.entry_fee = entry_fee
        self.tambourine = tambourine
    
    def get_current_capacity(self):
        return len(self.current_guests)
    
    def guest_checks_in(self, guest, room):
        if len(self.current_guests) < self.capacity:
            guest.pay_entry(room)
            room.add_entry_fee_to_tab()
            self.current_guests.append(guest)
        else:
            return("not tonight pal")

    def guest_checks_out(self, guest):
        self.current_guests.remove(guest)

    def add_song(self, song):
        self.song_list.append(song)

    def add_entry_fee_to_tab(self):
        self.tab += self.entry_fee

    def add_drink(self, drink):
        self.drink_list.append(drink)

    def has_tambourine(self):
        if self.tambourine == True:
            return("yes, it has a tambourine!!")



