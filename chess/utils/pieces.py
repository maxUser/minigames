from utils.helper import (y_flip, letter_to_number, number_to_letter,
                         get_x_threat, get_y_threat)

class Piece:
    # every piece must carry with it the squares that it threatens.
    # no this cannot work because the squares a piece threatens changes if another piece is in the way.
    # this is only a problem for: rook, queen, bishop since they threaten squares in a continuous line.
    # solution: set the threatened squares for these pieces to be ...
    # we don't need to know what piece threatens a square, only that it is threatened. this means each team can
    # store the squares it threatens.
    # we still require each piece to hold a list of squares it threatens so we can update the threatened squares
    # in the team object.

    def __str__(self):
        return self.team + ' ' + self.type + ' @ ' + self.pos

    def __init__(self, type, team, pos):
        """
            type (str): ex. pawn, rook, knight, bishop, king, or queen
            team (str): ex. cyan, yellow
            pos (str): ex. b2
            initial_pos (bool): if the piece has moved or not
            threatened (bool): if the piece is in danger of being taken
            threatening (list): all squares this piece threatens determined by its current position
        """
        self.type = type
        self.team = team
        self.pos = pos
        self.threatening = []
        self.initial_pos = True
        self.threatened = False

    def calculate_threat(self, squares):
        """ this function needs to be called every time a piece is moved
        """

        if self.threatening:
            # TODO: update team threat here
            self.threatening = []
        

        x = letter_to_number(self.pos[0])
        y = y_flip(self.pos[1])
        if self.type == 'pawn':
            if self.team == 'cyan':
                up_left = ()
                up_right = ()
                if x-1 > -1:
                    up_left = (number_to_letter(x-1) + str(y_flip(y-1)))
                if x+1 < 8:
                    up_right = (number_to_letter(x+1) + str(y_flip(y-1)))
                
                if up_left:
                    self.threatening.append(up_left)
                if up_right:
                    self.threatening.append(up_right)
            elif self.team == 'yellow':
                down_left = ()
                down_right = ()
                if x-1 > -1:
                    down_left = (number_to_letter(x-1) + str(y_flip(y+1)))
                if x+1 < 8:
                    down_right = (number_to_letter(x+1) + str(y_flip(y+1)))
                
                if down_left:
                    self.threatening.append(down_left)
                if down_right:
                    self.threatening.append(down_right)
        
        elif self.type == 'rook':
            for threatened_square in get_x_threat(self.team, self.pos, squares):
                self.threatening.append(threatened_square)
            for threatened_square in get_y_threat(self.team, self.pos, squares):
                self.threatening.append(threatened_square)
            #print(get_y_threat(self.pos, squares))
            #print(self.threatening)
