class Guest:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def pay_entry(self):
        if self.wallet >= 10:
            self.wallet -= 10
        else:
            return("not tonight pal")

