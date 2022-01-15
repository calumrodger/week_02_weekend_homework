class Guest:

    def __init__(self, name, wallet, fav_song):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song

    def pay_entry(self):
        if self.wallet >= 10:
            self.wallet -= 10
        else:
            return("not tonight pal")

    def buy_drink(self, drink, room):
        if self.wallet >= drink.price:
            self.wallet -= drink.price
            room.tab += drink.price


    def guest_fav_song_is_on_list(self, room):
        for song in room.song_list:
            if song.name == self.fav_song.name:
                return("woot woot")