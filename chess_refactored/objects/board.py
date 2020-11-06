from objects.piece import Piece
from objects.team import Team

class Board:
    
    def __init__(self):
        self.squares = {'a1':None, 'a2':None, 'a3':None, 'a4':None, 'a5':None, 'a6':None, 'a7':None, 'a8':None,
               'b1':None, 'b2':None, 'b3':None, 'b4':None, 'b5':None, 'b6':None, 'b7':None, 'b8':None,
               'c1':None, 'c2':None, 'c3':None, 'c4':None, 'c5':None, 'c6':None, 'c7':None, 'c8':None,
               'd1':None, 'd2':None, 'd3':None, 'd4':None, 'd5':None, 'd6':None, 'd7':None, 'd8':None,
               'e1':None, 'e2':None, 'e3':None, 'e4':None, 'e5':None, 'e6':None, 'e7':None, 'e8':None,
               'f1':None, 'f2':None, 'f3':None, 'f4':None, 'f5':None, 'f6':None, 'f7':None, 'f8':None,
               'g1':None, 'g2':None, 'g3':None, 'g4':None, 'g5':None, 'g6':None, 'g7':None, 'g8':None,
               'h1':None, 'h2':None, 'h3':None, 'h4':None, 'h5':None, 'h6':None, 'h7':None, 'h8':None
               }

    def initialize(self, all_pieces):
        for team in all_pieces:
            for piece_type in team:
                for piece in piece_type:
                    self.squares[piece.pos] = piece

    def move_piece(self, piece, tar_pos):
        """
        Args:
            piece (obj) - the piece selected to move
            tar_pos (str) - the square selected to move the piece to
        """
        print('Moving {} to {}'.format(self.squares[piece.pos], tar_pos))
        self.squares[piece.pos] = None
        self.squares[tar_pos] = piece
        piece.pos = tar_pos
        piece.moved = True
        return piece 

    def print_board(self):
        for key, val in self.squares.items():
            if val is not None:
                print(key, val)


        