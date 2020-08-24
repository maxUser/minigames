class Piece:
    # every piece must carry with it the squares that it threatens

    initial_pos = True
    threatened = False

    # def move(self, new_pos):
    #     self.pos = [new_pos[0], new_pos[1]]

    def __str__(self):
        return self.team + ' ' + self.type

    def __init__(self, type, team):
        """
        type (str): ex. pawn, rook, knight, bishop, king, or queen
        team (str): ex. cyan, yellow
        """
        self.type = type
        self.team = team
