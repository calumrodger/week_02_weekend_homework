class Room:

    def __init__(self, name, capacity, tab):
        self.name = name
        self.capacity = capacity
        self.current_guests = []
        self.song_list = []
        self.tab = tab
        self.drink_list = []
    
    def get_current_capacity(self):
        return len(self.current_guests)
    
    def guest_checks_in(self, guest, room):
        if len(self.current_guests) < self.capacity:
            guest.pay_entry()
            room.add_entry_fee_to_tab()
            self.current_guests.append(guest)
        else:
            return("not tonight pal")

    def guest_checks_out(self, guest):
        self.current_guests.remove(guest)

    def add_song(self, song):
        self.song_list.append(song)

    def add_entry_fee_to_tab(self):
        self.tab += 10

    def add_drink(self, drink):
        self.drink_list.append(drink)



