from pieces import Piece

class Team:

    # teams = {
    #     'wh':{'pawns':[], 'rooks':[], 'knights':[], 'bishops':[], 'king':[], 'queen':[]},
    #     'bl':{'pawns':[], 'rooks':[], 'knights':[], 'bishops':[], 'king':[], 'queen':[]}
    #     }

    def __init__(self, colour):
        self.colour = colour
        self.army = {'pawns':[], 'rooks':[], 'knights':[], 'bishops':[], 'king':[], 'queen':[]}

    def populate(self):
        """ Create teams and fill each team with their pieces

        teams (dict): teams are wh (white) and bl (black). Each team
                      contains keys that correspond to the name of a
                      piece. The keys hold a list of objects
                      representing pieces according to their name.
        """

        print(self.army)

        # for team in self.teams:
            # pawns
        for i in range(8):
            type = 'pawn'
            t_pawn = Piece(type, self.colour, starting_pos(self.colour, type, i))
            # self.teams[team]['pawns'].append(t_pawn)
            self.army['pawns'].append(t_pawn)

        # rooks, knights, bishops
        types = ['rook', 'knight', 'bishop']
        for type in types:
            piece_pos1, piece_pos2 = starting_pos(self.colour, type, -1)
            piece1 = Piece(type, self.colour, piece_pos1)
            piece2 = Piece(type, self.colour, piece_pos2)
            if type == 'rook':
                self.army['rooks'].append(piece1)
                self.army['rooks'].append(piece2)
            elif type == 'knight':
                self.army['knights'].append(piece1)
                self.army['knights'].append(piece2)
            elif type == 'bishop':
                self.army['bishops'].append(piece1)
                self.army['bishops'].append(piece2)

        # king and queen
        types = ['king', 'queen']
        for type in types:
            piece_pos = starting_pos(self.colour, type, -1)
            piece = Piece(type, self.colour, piece_pos)
            if type == 'king':
                self.army[type].append(piece)
            if type == 'queen':
                self.army[type].append(piece)



def starting_pos(colour, type, i):
    #   0 1 2 3 4 5 6 7
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7

    if colour == 'wh':
        if type == 'pawn':
            return [i, 1]
        elif type == 'rook':
            return [0, 7], [7, 7]
        elif type == 'knight':
            return [1, 7], [6, 7]
        elif type == 'bishop':
            return [2, 7], [5, 7]
        elif type == 'king':
            return [4, 7]
        elif type == 'queen':
            return [3, 7]
    elif colour == 'bl':
        if type == 'pawn':
            return [i, 6]
        elif type == 'rook':
            return [0, 0], [0, 7]
        elif type == 'knight':
            return [0, 1], [0, 6]
        elif type == 'bishop':
            return [0, 2], [0, 5]
        elif type == 'king':
            return [0, 4]
        elif type == 'queen':
            return [0, 3]
