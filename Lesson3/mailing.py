from address import Address

class Mailing:
    
    to_address = ""
    from_address = ""
    cost = 0
    track = 0


    def setToAders(self, index, city, street, home, apartment):
        self.to_address = Address(index, city, street, home, apartment)

    def setFromAders(self, index, city, street, home, apartment):
        self.from_address = Address(index, city, street, home, apartment)

    def setCost(self, cost):
        self.cost = cost

    def setTrack(self, track):
        self.track = track