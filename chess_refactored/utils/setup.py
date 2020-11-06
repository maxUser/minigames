from utils.helper import number_to_letter
from objects.team import Team
from objects.board import Board
from objects.piece import Piece

def setup_game():
    # create board
    board = Board()
    # create teams
    white = Team('white')
    black = Team('black')
    teams = (white, black)
    # create pieces
    white_pawns = [Piece(white, 'pawn', number_to_letter(i)+str(2), 'p') for i in range(1, 9)]
    black_pawns = [Piece(black, 'pawn', number_to_letter(i)+str(7), 'P') for i in range(1, 9)]
    white_rooks = [Piece(white, 'rook', number_to_letter(i)+str(1), 'r') for i in range(1, 9, 7)]
    black_rooks = [Piece(black, 'rook', number_to_letter(i)+str(8), 'R') for i in range(1, 9, 7)]
    white_knights = [Piece(white, 'knight', number_to_letter(i)+str(1), 'n') for i in range(2, 8, 5)]
    black_knights = [Piece(black, 'knight', number_to_letter(i)+str(8), 'N') for i in range(2, 8, 5)]
    white_bishops = [Piece(white, 'bishop', number_to_letter(i)+str(1), 'b') for i in range(3, 7, 3)]
    black_bishops = [Piece(black, 'bishop', number_to_letter(i)+str(8), 'B') for i in range(3, 7, 3)]
    white_queen = [Piece(white, 'queen', 'd1', 'q')]
    black_queen = [Piece(black, 'queen', 'd8', 'Q')]
    white_king = [Piece(white, 'king', 'e1', 'k')]
    black_king = [Piece(black, 'king', 'e8', 'K')]
    white_pieces = [white_pawns, white_rooks, white_knights, white_bishops, white_queen, white_king]
    black_pieces = [black_pawns, black_rooks, black_knights, black_bishops, black_queen, black_king]
    # initialize teams
    white.initialize(white_pieces)
    black.initialize(black_pieces)
    # initialize board
    board.initialize((white_pieces, black_pieces))

    return board, teams