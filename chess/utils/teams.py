class Team:
    # still need algorithm to determine which squares a piece threatens given its current position.
    # store all squares threatened by a team here

    def __init__(self, colour):
        self.colour = colour
        self.graveyard = []
        self.threatening = []


    def add_threat(self, threat_list):
        for threatened_square in threat_list:
            self.threatening.append(threatened_square)

    def remove_threat(self, threat_list):
        for free_square in threat_list:
            self.threatening.remove(free_square)