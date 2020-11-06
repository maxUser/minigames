from utils.setup import setup_game
from utils.helper import (number_to_letter, piece_to_move_prompt, 
                        target_square_prompt, get_piece_to_move,
                        check_move_legality, move_or_take)

def run_game():
    board, teams = setup_game()
    win = False
    i = 0
    while win is False:
        team = teams[i%2]
        oppo_team = teams[(i+1)%2]
        print('\n{}\'s turn\n'.format(team.colour))

        # Get input
        piece_to_move = get_piece_to_move(piece_to_move_prompt(), team)
        target = target_square_prompt()
        # Check input
        legal = check_move_legality(board, piece_to_move, target)
        # Act on input
        if legal is True:
            move_or_take = move_or_take(board, piece_to_move, target)
            board.move_piece(piece_to_move, target)
            i+=1
        else:
            print('Illegal move. Try again.')

def run_game_test(board, team, a, b):
    """
    Args:
        team (obj) - the team whose piece is being manipulated
        a (str) - square containing piece to move
        b (str) - target square
    """
    piece_to_move = get_piece_to_move(a, team)
    legal = check_move_legality(board, piece_to_move, b)
    if legal is True:
        board.move_piece(piece_to_move, b)
    
    return board, team, piece_to_move, legal

    

    

