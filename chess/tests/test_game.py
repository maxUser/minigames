from utils.game import (player_move, y_flip, letter_to_number,
                 check_move, pawn_rules, get_oppo_team,
                 get_piece_to_move, get_target_position,
                 act_on_result, get_x_between, get_y_between)
from utils.board import Board
from utils.teams import Team
import utils.game as game
import pytest


ye_team = Team('yellow')
cy_team = Team('cyan')
board = Board()

# A
def selectA1():
    return 'a1'
def selectA2():
    return 'a2'
def selectA3():
    return 'a3'
def selectA4():
    return 'a4'
def selectA5():
    return 'a5'
def selectA6():
    return 'a6'
def selectA7():
    return 'a7'
def selectA8():
    return 'a8'
# B
def selectB1():
    return 'b1'
def selectB2():
    return 'b2'
def selectB3():
    return 'b3'
def selectB4():
    return 'b4'
def selectB5():
    return 'b5'
def selectB6():
    return 'b6'
def selectB7():
    return 'b7'
def selectB8():
    return 'b8'
# C
def selectC1():
    return 'c1'
def selectC2():
    return 'c2'
def selectC3():
    return 'c3'
def selectC4():
    return 'c4'
def selectC5():
    return 'c5'
def selectC6():
    return 'c6'
def selectC7():
    return 'c7'
def selectC8():
    return 'c8'
# D
def selectD1():
    return 'd1'
def selectD2():
    return 'd2'
def selectD3():
    return 'd3'
def selectD4():
    return 'd4'
def selectD5():
    return 'd5'
def selectD6():
    return 'd6'
def selectD7():
    return 'd7'
def selectD8():
    return 'd8'
# E
def selectE1():
    return 'e1'
def selectE2():
    return 'e2'
def selectE3():
    return 'e3'
def selectE4():
    return 'e4'
def selectE5():
    return 'e5'
def selectE6():
    return 'e6'
def selectE7():
    return 'e7'
def selectE8():
    return 'e8'
# F
def selectF1():
    return 'f1'
def selectF2():
    return 'f2'
def selectF3():
    return 'f3'
def selectF4():
    return 'f4'
def selectF5():
    return 'f5'
def selectF6():
    return 'f6'
def selectF7():
    return 'f7'
def selectF8():
    return 'f8'
# G
def selectG1():
    return 'g1'
def selectG2():
    return 'g2'
def selectG3():
    return 'g3'
def selectG4():
    return 'g4'
def selectG5():
    return 'g5'
def selectG6():
    return 'g6'
def selectG7():
    return 'g7'
def selectG8():
    return 'g8'
# H
def selectH1():
    return 'h1'
def selectH2():
    return 'h2'
def selectH3():
    return 'h3'
def selectH4():
    return 'h4'
def selectH5():
    return 'h5'
def selectH6():
    return 'h6'
def selectH7():
    return 'h7'
def selectH8():
    return 'h8'


class TestUtility:

    @pytest.mark.yBetween
    def test_get_between_straight(self):
        print('ybetween')
        betweeners = get_y_between(['1', '7'])
        assert betweeners == [2,3,4,5,6,7]

    @pytest.mark.xBetween
    def test_get_between_lateral(self):
        betweeners = get_x_between(['a', 'h'])
        assert betweeners == ['b', 'c', 'd', 'e', 'f', 'g', 'h']

    @pytest.mark.take
    def test_taking_pieces(self, monkeypatch):
        board.reset_game()

        monkeypatch.setattr(game, 'get_piece_to_move', selectD2)
        monkeypatch.setattr(game, 'get_target_position', selectD4)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectE7)
        monkeypatch.setattr(game, 'get_target_position', selectE5)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(ye_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, ye_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectD4)
        monkeypatch.setattr(game, 'get_target_position', selectE5)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        assert result == 1





class TestPieceMovement:
    """
        Notes: Call board.reset_game() at the start of every test
    """

    """
    QUEEN TESTS
    """
    def test_queen_lateral_move(self, monkeypatch):
        board.reset_game()

        monkeypatch.setattr(game, 'get_piece_to_move', selectD2)
        monkeypatch.setattr(game, 'get_target_position', selectD4)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectD1)
        monkeypatch.setattr(game, 'get_target_position', selectD3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectD3)
        monkeypatch.setattr(game, 'get_target_position', selectG3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        assert result == 1

    def test_queen_diagonal_move(self, monkeypatch):
        board.reset_game()

        monkeypatch.setattr(game, 'get_piece_to_move', selectD2)
        monkeypatch.setattr(game, 'get_target_position', selectD4)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectD1)
        monkeypatch.setattr(game, 'get_target_position', selectD3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectD3)
        monkeypatch.setattr(game, 'get_target_position', selectG6)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        assert result == 1

    def test_queen_bad_move(self, monkeypatch):
        board.reset_game()

        monkeypatch.setattr(game, 'get_piece_to_move', selectD2)
        monkeypatch.setattr(game, 'get_target_position', selectD4)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectD1)
        monkeypatch.setattr(game, 'get_target_position', selectE3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        assert result == 0

    """
    KING TESTS
    """
    def test_kingside_castle(self, monkeypatch):
        board.reset_game()
        monkeypatch.setattr(game, 'get_piece_to_move', selectG1)
        monkeypatch.setattr(game, 'get_target_position', selectF3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectG2)
        monkeypatch.setattr(game, 'get_target_position', selectG3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectF1)
        monkeypatch.setattr(game, 'get_target_position', selectH3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectE1)
        monkeypatch.setattr(game, 'get_target_position', selectG1)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        assert result == 1

    def test_yeKing_move(self, monkeypatch):
        board.reset_game()
        monkeypatch.setattr(game, 'get_piece_to_move', selectE7)
        monkeypatch.setattr(game, 'get_target_position', selectE5)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(ye_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectE8)
        monkeypatch.setattr(game, 'get_target_position', selectE7)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(ye_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        assert result == 1

    def test_cyKing_move(self, monkeypatch):
        board.reset_game()
        monkeypatch.setattr(game, 'get_piece_to_move', selectE2)
        monkeypatch.setattr(game, 'get_target_position', selectE4)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectE1)
        monkeypatch.setattr(game, 'get_target_position', selectE2)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        assert result == 1


    def test_king_straight_move_fail(self, monkeypatch):
        board.reset_game()

        monkeypatch.setattr(game, 'get_piece_to_move', selectE2)
        monkeypatch.setattr(game, 'get_target_position', selectE4)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectE1)
        monkeypatch.setattr(game, 'get_target_position', selectE3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        assert result == 0

    def test_king_lateral_move_fail(self, monkeypatch):
        board.reset_game()

        monkeypatch.setattr(game, 'get_piece_to_move', selectE2)
        monkeypatch.setattr(game, 'get_target_position', selectE4)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectE1)
        monkeypatch.setattr(game, 'get_target_position', selectE2)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectE2)
        monkeypatch.setattr(game, 'get_target_position', selectE3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectE3)
        monkeypatch.setattr(game, 'get_target_position', selectA3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        assert result == 0


    """
    BISHOP TESTS
    """
    def test_bishop_bad_move(self, monkeypatch):
        board.reset_game()

        monkeypatch.setattr(game, 'get_piece_to_move', selectD2)
        monkeypatch.setattr(game, 'get_target_position', selectD3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectC1)
        monkeypatch.setattr(game, 'get_target_position', selectE3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectE3)
        monkeypatch.setattr(game, 'get_target_position', selectF5)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        assert result == 0


    def test_bishop_lateral_move(self, monkeypatch):
        board.reset_game()

        monkeypatch.setattr(game, 'get_piece_to_move', selectD2)
        monkeypatch.setattr(game, 'get_target_position', selectD3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectC1)
        monkeypatch.setattr(game, 'get_target_position', selectE3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectE3)
        monkeypatch.setattr(game, 'get_target_position', selectH3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        assert result == 0

    def test_bishop_straight_move(self, monkeypatch):
        board.reset_game()

        monkeypatch.setattr(game, 'get_piece_to_move', selectC2)
        monkeypatch.setattr(game, 'get_target_position', selectC4)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectC1)
        monkeypatch.setattr(game, 'get_target_position', selectC3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        assert result == 0

    """
    KNIGHT TESTS
    """
    def test_yeKnight_move_far_fail(self, monkeypatch):
        board.reset_game()

        monkeypatch.setattr(game, 'get_piece_to_move', selectG8)
        monkeypatch.setattr(game, 'get_target_position', selectF3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(ye_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, ye_team)

        assert result == 0

    def test_yeKnight_move_straight_fail(self, monkeypatch):
        board.reset_game()

        monkeypatch.setattr(game, 'get_piece_to_move', selectG8)
        monkeypatch.setattr(game, 'get_target_position', selectF6)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(ye_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, ye_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectF6)
        monkeypatch.setattr(game, 'get_target_position', selectF8)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(ye_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, ye_team)

        assert result == 0

    def test_yeKnight_move(self, monkeypatch):
        board.reset_game()

        monkeypatch.setattr(game, 'get_piece_to_move', selectG8)
        monkeypatch.setattr(game, 'get_target_position', selectF6)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(ye_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, ye_team)

        assert result == 1

    def test_cyKnight_move(self, monkeypatch):
        board.reset_game()

        monkeypatch.setattr(game, 'get_piece_to_move', selectB1)
        monkeypatch.setattr(game, 'get_target_position', selectC3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        assert result == 1

    """
    ROOK TESTS
    """
    def test_rook_diagonal_move(self, monkeypatch):
        board.reset_game()

        monkeypatch.setattr(game, 'get_piece_to_move', selectA2)
        monkeypatch.setattr(game, 'get_target_position', selectA4)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectA1)
        monkeypatch.setattr(game, 'get_target_position', selectA3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectA3)
        monkeypatch.setattr(game, 'get_target_position', selectC5)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        assert result == 0

    def test_rook_lateral_move(self, monkeypatch):
        board.reset_game()

        monkeypatch.setattr(game, 'get_piece_to_move', selectH2)
        monkeypatch.setattr(game, 'get_target_position', selectH4)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectH7)
        monkeypatch.setattr(game, 'get_target_position', selectH5)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(ye_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, ye_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectH1)
        monkeypatch.setattr(game, 'get_target_position', selectH3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectH8)
        monkeypatch.setattr(game, 'get_target_position', selectH6)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(ye_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, ye_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectH3)
        monkeypatch.setattr(game, 'get_target_position', selectC3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectH6)
        monkeypatch.setattr(game, 'get_target_position', selectD6)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(ye_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, ye_team)

        assert result == 1

    """
    PAWN TESTS
    """

    def test_pawn_diagonal_move(self, monkeypatch):
        board.reset_game()

        monkeypatch.setattr(game, 'get_piece_to_move', selectA2)
        monkeypatch.setattr(game, 'get_target_position', selectA3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectA3)
        monkeypatch.setattr(game, 'get_target_position', selectB4)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        assert result == 0

    def test_pawn_init_move(self, monkeypatch):
        board.reset_game()

        monkeypatch.setattr(game, 'get_piece_to_move', selectA2)
        monkeypatch.setattr(game, 'get_target_position', selectA3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectB2)
        monkeypatch.setattr(game, 'get_target_position', selectB4)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectA3)
        monkeypatch.setattr(game, 'get_target_position', selectA5)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        assert result == 0


    def test_cyPawn_take_yePawn(self, monkeypatch):
        board.reset_game()

        monkeypatch.setattr(game, 'get_piece_to_move', selectA2)
        monkeypatch.setattr(game, 'get_target_position', selectA4)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectB7)
        monkeypatch.setattr(game, 'get_target_position', selectB5)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(ye_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, ye_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectA4)
        monkeypatch.setattr(game, 'get_target_position', selectB5)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        assert result == 1

    def test_yePawn_take_cyPawn(self, monkeypatch):
        board.reset_game()

        monkeypatch.setattr(game, 'get_piece_to_move', selectA2)
        monkeypatch.setattr(game, 'get_target_position', selectA3)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectB7)
        monkeypatch.setattr(game, 'get_target_position', selectB5)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(ye_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, ye_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectA3)
        monkeypatch.setattr(game, 'get_target_position', selectA4)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectB5)
        monkeypatch.setattr(game, 'get_target_position', selectA4)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(ye_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, ye_team)

        assert result == 1

    def test_pawn_headOn_collision(self, monkeypatch):
        board.reset_game()

        monkeypatch.setattr(game, 'get_piece_to_move', selectA2)
        monkeypatch.setattr(game, 'get_target_position', selectA4)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectA7)
        monkeypatch.setattr(game, 'get_target_position', selectA5)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(ye_team)
        act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, ye_team)

        monkeypatch.setattr(game, 'get_piece_to_move', selectA4)
        monkeypatch.setattr(game, 'get_target_position', selectA5)
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(cy_team)
        result = act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, cy_team)

        assert result == 0
