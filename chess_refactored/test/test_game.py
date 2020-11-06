import pytest
from utils.setup import setup_game
from utils.game import run_game_test

class TestObjectsUpdatingAfterMovement:
    def test_board_team_piece_update_white(self):
        board, teams = setup_game()
        white = teams[0]
        board, white, piece_to_move, legal = run_game_test(board, white, 'a2', 'a4')
        assert board.squares['a4'] is not None and piece_to_move.pos == 'a4' and board.squares['a2'] is None and [piece for piece in white.pieces if piece.pos == 'a4']
    
    def test_board_team_piece_update_black(self):
        board, teams = setup_game()
        black = teams[1]
        board, black, piece_to_move, legal = run_game_test(board, black, 'b8', 'a6')
        assert board.squares['a6'] is not None and board.squares['b8'] is None and piece_to_move.pos == 'a6' and [piece for piece in black.pieces if piece.pos == 'a6']

class TestPieceRules:
    @pytest.mark.pawn
    def test_pawn_backward_white(self):
        board, teams = setup_game()
        white = teams[0]
        board, white, piece_to_move, legal = run_game_test(board, white, 'a2', 'a4')
        board, white, piece_to_move, legal = run_game_test(board, white, 'a4', 'a3')
        assert legal == False

    @pytest.mark.pawn
    def test_pawn_diagonal_white(self):
        board, teams = setup_game()
        white = teams[0]
        board, white, piece_to_move, legal = run_game_test(board, white, 'a2', 'b3')
        assert legal == False


    

