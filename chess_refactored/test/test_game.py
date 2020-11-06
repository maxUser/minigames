import pytest
from utils.setup import setup_game
from utils.game import run_game_test

class TestKnightRules:
    @pytest.mark.knight
    def test_knight_good_move_white(self):
        board, teams = setup_game()
        white = teams[0]
        board, white, piece_to_move, legal = run_game_test(board, white, 'b1', 'c3')
        assert legal == True

    @pytest.mark.knight
    def test_knight_good_move2_white(self):
        board, teams = setup_game()
        white = teams[0]
        board, white, piece_to_move, legal = run_game_test(board, white, 'b1', 'c3')
        board, white, piece_to_move, legal = run_game_test(board, white, 'c3', 'e4')
        assert legal == True

    @pytest.mark.knight
    def test_knight_good_move_black(self):
        board, teams = setup_game()
        black = teams[1]
        board, black, piece_to_move, legal = run_game_test(board, black, 'g8', 'f6')
        assert legal == True

    @pytest.mark.knight
    def test_knight_good_move2_black(self):
        board, teams = setup_game()
        black = teams[1]
        board, black, piece_to_move, legal = run_game_test(board, black, 'b8', 'a6')
        board, black, piece_to_move, legal = run_game_test(board, black, 'a6', 'c5')
        assert legal == True

    @pytest.mark.knight
    def test_knight_bad_move_white(self):
        board, teams = setup_game()
        white = teams[0]
        board, white, piece_to_move, legal = run_game_test(board, white, 'b1', 'b3')
        assert legal == False

    @pytest.mark.knight
    def test_knight_bad_move_black(self):
        board, teams = setup_game()
        black = teams[1]
        board, black, piece_to_move, legal = run_game_test(board, black, 'b8', 'c5')
        assert legal == False

class TestRookRules:
    @pytest.mark.rook
    def test_rook_diagonal_white(self):
        board, teams = setup_game()
        white = teams[0]
        board, white, piece_to_move, legal = run_game_test(board, white, 'a2', 'a4')
        board, white, piece_to_move, legal = run_game_test(board, white, 'a1', 'a3')
        board, white, piece_to_move, legal = run_game_test(board, white, 'a3', 'd6')
        assert legal == False
    
    @pytest.mark.rook
    def test_rook_diagonal_black(self):
        board, teams = setup_game()
        black = teams[1]
        board, black, piece_to_move, legal = run_game_test(board, black, 'h7', 'h5')
        board, black, piece_to_move, legal = run_game_test(board, black, 'h8', 'h6')
        board, black, piece_to_move, legal = run_game_test(board, black, 'h6', 'g5')
        assert legal == False

    @pytest.mark.rook
    def test_rook_lateral_black(self):
        board, teams = setup_game()
        black = teams[1]
        board, black, piece_to_move, legal = run_game_test(board, black, 'h7', 'h5')
        board, black, piece_to_move, legal = run_game_test(board, black, 'h8', 'h6')
        board, black, piece_to_move, legal = run_game_test(board, black, 'h6', 'c6')
        assert legal == True

class TestPawnRules:
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

    @pytest.mark.pawn
    def test_pawn_lateral_white(self):
        board, teams = setup_game()
        white = teams[0]
        board, white, piece_to_move, legal = run_game_test(board, white, 'a2', 'a3')
        board, white, piece_to_move, legal = run_game_test(board, white, 'a3', 'c3')
        assert legal == False

    @pytest.mark.pawn
    def test_pawn_illegal_double_move_white(self):
        board, teams = setup_game()
        white = teams[0]
        board, white, piece_to_move, legal = run_game_test(board, white, 'c2', 'c3')
        board, white, piece_to_move, legal = run_game_test(board, white, 'c3', 'c5')
        assert legal == False

    @pytest.mark.pawn
    def test_pawn_illegal_triple_move_white(self):
        board, teams = setup_game()
        white = teams[0]
        board, white, piece_to_move, legal = run_game_test(board, white, 'c2', 'c5')
        assert legal == False

    @pytest.mark.pawn
    def test_pawn_take_straight_ahead_white(self):
        board, teams = setup_game()
        white = teams[0]
        black = teams[1]
        board, white, piece_to_move, legal = run_game_test(board, white, 'c2', 'c4')
        board, black, piece_to_move, legal = run_game_test(board, black, 'c7', 'c5')
        board, white, piece_to_move, legal = run_game_test(board, white, 'c4', 'c5')
        assert legal == False

    @pytest.mark.pawn
    def test_pawn_take_pawn_white(self):
        board, teams = setup_game()
        white = teams[0]
        black = teams[1]
        board, white, piece_to_move, legal = run_game_test(board, white, 'c2', 'c4')
        board, black, piece_to_move, legal = run_game_test(board, black, 'b7', 'c5')
        board, white, piece_to_move, legal = run_game_test(board, white, 'c4', 'c5')
        assert legal == True

    @pytest.mark.pawn
    def test_pawn_take_same_team_pawn_white(self):
        board, teams = setup_game()
        white = teams[0]
        board, white, piece_to_move, legal = run_game_test(board, white, 'c2', 'c3')
        board, white, piece_to_move, legal = run_game_test(board, white, 'b2', 'c3')
        assert legal == False

    @pytest.mark.pawn
    def test_pawn_backward_black(self):
        board, teams = setup_game()
        black = teams[1]
        board, black, piece_to_move, legal = run_game_test(board, black, 'a7', 'a5')
        board, black, piece_to_move, legal = run_game_test(board, black, 'a5', 'a6')
        assert legal == False

    @pytest.mark.pawn
    def test_pawn_diagonal_black(self):
        board, teams = setup_game()
        black = teams[1]
        board, black, piece_to_move, legal = run_game_test(board, black, 'a7', 'b6')
        assert legal == False

    @pytest.mark.pawn
    def test_pawn_lateral_black(self):
        board, teams = setup_game()
        black = teams[1]
        board, black, piece_to_move, legal = run_game_test(board, black, 'a7', 'a6')
        board, black, piece_to_move, legal = run_game_test(board, black, 'a6', 'c6')
        assert legal == False

    @pytest.mark.pawn
    def test_pawn_illegal_double_move_black(self):
        board, teams = setup_game()
        black = teams[1]
        board, black, piece_to_move, legal = run_game_test(board, black, 'c7', 'c6')
        board, black, piece_to_move, legal = run_game_test(board, black, 'c6', 'c4')
        assert legal == False

    @pytest.mark.pawn
    def test_pawn_illegal_triple_move_black(self):
        board, teams = setup_game()
        black = teams[1]
        board, black, piece_to_move, legal = run_game_test(board, black, 'c7', 'c4')
        assert legal == False

    @pytest.mark.pawn
    def test_pawn_take_straight_ahead_black(self):
        board, teams = setup_game()
        white = teams[0]
        black = teams[1]
        board, black, piece_to_move, legal = run_game_test(board, black, 'c7', 'c5')
        board, white, piece_to_move, legal = run_game_test(board, white, 'c2', 'c4')
        board, black, piece_to_move, legal = run_game_test(board, black, 'c5', 'c4')
        assert legal == False

    @pytest.mark.pawn
    def test_pawn_take_pawn_black(self):
        board, teams = setup_game()
        white = teams[0]
        black = teams[1]
        board, black, piece_to_move, legal = run_game_test(board, black, 'c7', 'c5')
        board, white, piece_to_move, legal = run_game_test(board, white, 'b2', 'c4')
        board, black, piece_to_move, legal = run_game_test(board, black, 'c5', 'c4')
        assert legal == True

    @pytest.mark.pawn
    def test_pawn_take_same_team_pawn_black(self):
        board, teams = setup_game()
        black = teams[0]
        board, black, piece_to_move, legal = run_game_test(board, black, 'c7', 'c6')
        board, black, piece_to_move, legal = run_game_test(board, black, 'b7', 'c6')
        assert legal == False

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

class TestSelection:
    def test_select_empty_square_white(self):
        board, teams = setup_game()
        white = teams[0]
        board, white, piece_to_move, legal = run_game_test(board, white, 'a3', 'a4')
        assert legal == False

    def test_select_empty_square_black(self):
        board, teams = setup_game()
        black = teams[1]
        board, black, piece_to_move, legal = run_game_test(board, black, 'b6', 'b4')
        assert legal == False