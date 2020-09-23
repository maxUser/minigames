class Team:

    def __init__(self, colour):
        self.colour = colour
        self.graveyard = []
        self.threatening = []
        self.pieces = []


    def add_threat(self, threat_list):
        for threatened_square in threat_list:
            self.threatening.append(threatened_square)

    def remove_threat(self, threat_list):
        for free_square in threat_list:
            if free_square in self.threatening:
                self.threatening.remove(free_square)
    
    def add_piece(self, piece):
        self.pieces.append(piece)