class Room:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.current_guests = []
        self.song_list = []
    
    def get_current_capacity(self):
        return len(self.current_guests)
    
    def guest_checks_in(self, guest):
        if len(self.current_guests) < self.capacity:
            guest.pay_entry()
            self.current_guests.append(guest)
        else:
            return("not tonight pal")
        

    def guest_checks_out(self, guest):
        self.current_guests.remove(guest)

    def add_song(self, song):
        self.song_list.append(song)

