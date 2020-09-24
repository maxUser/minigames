from termcolor import colored
from utils.pieces import Piece
from utils.teams import Team
import re


class Board:
    """A representation of the board
    - Bottom and left axes: what the player sees
    - Top and right axes: what the computer sees
      |0|1|2|3|4|5|6|7|
     8| | | | | | | | |0
     7| | | | | | | | |1
     6| | | | | | | | |2
     5| | | | | | | | |3
     4| | | | | | | | |4
     3| | | | | | | | |5
     2| | | | | | | | |6
     1| | | | | | | | |7
       a b c d e f g h
    """

    squares = {'a1':'', 'a2':'', 'a3':'', 'a4':'', 'a5':'', 'a6':'', 'a7':'', 'a8':'',
               'b1':'', 'b2':'', 'b3':'', 'b4':'', 'b5':'', 'b6':'', 'b7':'', 'b8':'',
               'c1':'', 'c2':'', 'c3':'', 'c4':'', 'c5':'', 'c6':'', 'c7':'', 'c8':'',
               'd1':'', 'd2':'', 'd3':'', 'd4':'', 'd5':'', 'd6':'', 'd7':'', 'd8':'',
               'e1':'', 'e2':'', 'e3':'', 'e4':'', 'e5':'', 'e6':'', 'e7':'', 'e8':'',
               'f1':'', 'f2':'', 'f3':'', 'f4':'', 'f5':'', 'f6':'', 'f7':'', 'f8':'',
               'g1':'', 'g2':'', 'g3':'', 'g4':'', 'g5':'', 'g6':'', 'g7':'', 'g8':'',
               'h1':'', 'h2':'', 'h3':'', 'h4':'', 'h5':'', 'h6':'', 'h7':'', 'h8':''
               }

    board = [
                ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
                ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
            ]

    def reset_game(self):
        for key, value in self.squares.items():
            self.squares[key] = ''

        self.board = [
                    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
                    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
                ]
        #self.initialize_squares()

    def initialize_squares(self, teams):
        """
            Args: 
                teams: tuple containing both teams.
        """
        cy_team = teams[0]
        ye_team = teams[1]
        cyan_pawn = re.compile('[a-h]2')
        cyan_rook = re.compile('(a1|h1)')
        cyan_knight = re.compile('(b1|g1)')
        cyan_bishop = re.compile('(c1|f1)')
        yellow_pawn = re.compile('[a-h]7')
        yellow_rook = re.compile('(a8|h8)')
        yellow_knight = re.compile('(b8|g8)')
        yellow_bishop = re.compile('(c8|f8)')

        for square in self.squares.keys():
            # CYAN
            if cyan_pawn.match(square):
                t_pawn = Piece('pawn', cy_team, square)
                cy_team.add_piece(t_pawn)
                self.squares[square] = t_pawn
            elif cyan_rook.match(square):
                t_rook = Piece('rook', cy_team, square)
                cy_team.add_piece(t_rook)
                self.squares[square] = t_rook
            elif cyan_knight.match(square):
                t_knight = Piece('knight', cy_team, square)
                cy_team.add_piece(t_knight)
                self.squares[square] = t_knight
            elif cyan_bishop.match(square):
                t_bishop = Piece('bishop', cy_team, square)
                cy_team.add_piece(t_bishop)
                self.squares[square] = t_bishop
            elif square == 'e1':
                t_king = Piece('king', cy_team, square)
                cy_team.add_piece(t_king)
                self.squares[square] = t_king
            elif square == 'd1':
                t_queen = Piece('queen', cy_team, square)
                cy_team.add_piece(t_queen)
                self.squares[square] = t_queen
            # YELLOW
            elif yellow_pawn.match(square):
                t_pawn = Piece('pawn', ye_team, square)
                ye_team.add_piece(t_pawn)
                self.squares[square] = t_pawn
            elif yellow_rook.match(square):
                t_rook = Piece('rook', ye_team, square)
                ye_team.add_piece(t_rook)
                self.squares[square] = t_rook
            elif yellow_knight.match(square):
                t_knight = Piece('knight', ye_team, square)
                ye_team.add_piece(t_knight)
                self.squares[square] = t_knight
            elif yellow_bishop.match(square):
                t_bishop = Piece('bishop', ye_team, square)
                ye_team.add_piece(t_bishop)
                self.squares[square] = t_bishop
            elif square == 'e8':
                t_king = Piece('king', ye_team, square)
                ye_team.add_piece(t_king)
                self.squares[square] = t_king
            elif square == 'd8':
                t_queen = Piece('queen', ye_team, square)
                ye_team.add_piece(t_queen)
                self.squares[square] = t_queen
        return cy_team, ye_team

    def print_squares(self):
        for key, value in self.squares.items():
            print(key, end=' ')
            print(value)

    def print_square(self, pos):
        return self.board[pos[1]][pos[0]]

    def move_piece(self, curr_pos, tar_pos, team):
        """ Change the internal representation of the board
        """
        self.squares[curr_pos].pos = tar_pos
        self.squares[tar_pos] = self.squares[curr_pos]
        self.squares[curr_pos] = ''   

    def alter(self, curr_pos, tar_pos):
        """ Change the print out of the board
        """
        piece = self.board[curr_pos[1]][curr_pos[0]]
        self.board[curr_pos[1]][curr_pos[0]] = ' '
        self.board[tar_pos[1]][tar_pos[0]] = piece

    def print_board(self):
        x_axis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        y_axis = ['8', '7', '6', '5', '4', '3', '2', '1']

        print('  ===================================')

        axis_count = 0
        for row in self.board:
            print(y_axis[axis_count]+' ||', end=' ')
            last_col = 0
            for square in row:
                if square.isupper():
                    print(colored(square, 'yellow'), end=' ')
                else:
                    print(colored(square, 'cyan'), end=' ')
                if last_col == 7:
                    print('||')
                else:
                    print('|', end=' ')
                last_col += 1


            if axis_count == 7:
                print('  ===================================')
            else:
                print('  -----------------------------------')
            axis_count += 1

        for x in x_axis:
            if x == 'a':
                print('     '+x, end=' ')
            else:
                print('  '+x, end=' ')
        print()
