from utils.helper import (y_flip, letter_to_number, number_to_letter,
                         get_x_threat, get_y_threat, get_L_threat,
                         get_diagonal_threat, get_queen_threat,
                         get_king_threat)

class Piece:

    def __str__(self):
        return self.team.colour + ' ' + self.type + ' @ ' + self.pos

    def __init__(self, type, team, pos):
        """
            type (str): ex. pawn, rook, knight, bishop, king, or queen
            team (teams obj): instance of Team class
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
        self.threatened = False # currently unused

    def calculate_threat(self, squares):
        if self.pos == 'graveyard':
            self.threatening = []
            return
        
        if self.threatening:
            self.threatening = []
       
        x = letter_to_number(self.pos[0])
        y = y_flip(self.pos[1])
        if self.type == 'pawn':
            if self.team.colour == 'cyan':
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
                
            elif self.team.colour == 'yellow':
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
        
        elif self.type == 'knight':
            for threatened_square in get_L_threat(self.team, self.pos, squares):
                self.threatening.append(threatened_square)

        elif self.type == 'bishop':
            for threatened_square in get_diagonal_threat(self.team, self.pos, squares):
                self.threatening.append(threatened_square)

        elif self.type == 'queen':
            for threatened_square in get_queen_threat(self.team, self.pos, squares):
                self.threatening.append(threatened_square)

        elif self.type == 'king':
            for threatened_square in get_king_threat(self.pos):
                self.threatening.append(threatened_square)
            #print('{} {} threats: {}'.format(self.team.colour, self.type, get_king_threat(self.team, self.pos, squares)))
        
