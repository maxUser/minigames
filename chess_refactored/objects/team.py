class Team:

    def __init__(self, colour):
        self.threatening = []
        self.pieces = []
        self.graveyard = []
        self.check = False
        self.colour = colour

    def initialize(self, all_pieces):
        for piece_type in all_pieces:
            for piece in piece_type:
                self.pieces.append(piece)
