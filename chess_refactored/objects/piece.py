class Piece:

    def __init__(self, team, type, pos, symbol):
        self.team = team
        self.type = type
        self.pos = pos
        self.symbol = symbol
        self.threatened = False
        self.threatening = []
        self.moved = False # for castling

    def __str__(self):
        # return self.team.colour + ' ' + self.type + ' (' + self.pos + ')'
        return self.pos + ' (' + self.team.colour + ' ' + self.type + ')'
