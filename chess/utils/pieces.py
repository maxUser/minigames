class Piece:
    # every piece must carry with it the squares that it threatens.
    # no this cannot work because the squares a piece threatens changes if another piece is in the way.
    # this is only a problem for: rook, queen, bishop since they threaten squares in a continuous line.
    # solution: set the threatened squares for these pieces to be ...
    # we don't need to know what piece threatens a square, only that it is threatened. this means each team can
    # store the squares it threatens.
    # we still require each piece to hold a list of squares it threatens so we can update the threatened squares
    # in the team object.

    initial_pos = True
    threatened = False
    threatening = []

    def __str__(self):
        return self.team + ' ' + self.type + ' @ ' + self.pos

    def __init__(self, type, team, pos):
        """
        type (str): ex. pawn, rook, knight, bishop, king, or queen
        team (str): ex. cyan, yellow
        """
        self.type = type
        self.team = team
        self.pos = pos
