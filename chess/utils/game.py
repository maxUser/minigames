from utils.pieces import Piece
from utils.board import Board
from utils.teams import Team
from termcolor import colored
from utils.helper import (y_flip, get_x_between, get_y_between,
                          letter_to_number, number_to_letter,
                          print_error, get_piece_to_move,
                          get_target_position, update_team_threat,
                          checkmate, get_between_exclusive, check_move)

board = Board()

def player_move(team, oppo_team):
    print(colored(team.colour + '\'s turn', team.colour))

    curr_pos = get_piece_to_move()
    tar_pos = get_target_position()

    result = check_move(team, oppo_team, curr_pos, tar_pos, board)

    return result, curr_pos, tar_pos

def act_on_result(result, curr_pos, tar_pos, team):
    """ 
        Takes result of player_move and check_move functions
        to determine next action

        Return: 0 if move is invalid (same player's turn)
                1 if move is valid (next player's turn)
    """
    curr_x_y = [letter_to_number(curr_pos[0]), y_flip(curr_pos[1])]
    tar_x_y = [letter_to_number(tar_pos[0]), y_flip(tar_pos[1])]
    #print('Result: {}'.format(result))
    if result == 'ff':
        print_error('Target square occupied by friendly piece')
        return 0

    elif result == 'illegal':
        print_error('Illegal move: ' + curr_pos + ' to ' + tar_pos)
        return 0

    elif result == 'selection_error':
        print_error('{} is an invalid selection'.format(curr_pos))
        return 0

    elif result == 'invalid_input':
        print_error('Invalid input')
        return 0

    elif result == 'kingside_castle':
        board.squares[curr_pos].initial_pos = False
        board.squares[number_to_letter(curr_x_y[0]+3) + curr_pos[1]].initial_pos = False
        # move king
        board.alter(curr_x_y, tar_x_y)
        board.move_piece(curr_pos, tar_pos)
        # move rook
        board.alter([curr_x_y[0]+3, curr_x_y[1]], [curr_x_y[0]+1, curr_x_y[1]])
        board.move_piece(number_to_letter(curr_x_y[0]+3) + curr_pos[1], number_to_letter(curr_x_y[0]+1) + curr_pos[1])
        return 1
    
    elif result == 'queenside_castle':
        board.squares[curr_pos].initial_pos = False
        board.squares[number_to_letter(curr_x_y[0]-4) + curr_pos[1]].initial_pos = False
        # move king
        board.alter(curr_x_y, tar_x_y)
        board.move_piece(curr_pos, tar_pos)
        # move rook
        board.alter([curr_x_y[0]-4, curr_x_y[1]], [curr_x_y[0]-1, curr_x_y[1]])
        board.move_piece(number_to_letter(curr_x_y[0]-4) + curr_pos[1], number_to_letter(curr_x_y[0]-1) + curr_pos[1])
        return 1

    elif result == 'take':
        print('Taking piece at: ' + tar_pos)
        if board.squares[curr_pos].initial_pos == True:
            board.squares[curr_pos].initial_pos = False

        # update print out of board
        board.alter(curr_x_y, tar_x_y)
        # remove position from taken piece
        board.squares[tar_pos].pos = 'graveyard'
        # update internal representation of board
        board.move_piece(curr_pos, tar_pos)

        print('{} threatening {}'.format(board.squares[tar_pos], board.squares[tar_pos].threatening))

        return 1

    elif result == 'move':
        print('Moving {} to {}'.format(board.squares[curr_pos], tar_pos))
        if board.squares[curr_pos].initial_pos == True:
            board.squares[curr_pos].initial_pos = False
        
        # update print out of board
        board.alter(curr_x_y, tar_x_y)
        # update internal representation of board
        board.move_piece(curr_pos, tar_pos)   

        return 1

def testing_environment():
    cy_team = Team('cyan')
    ye_team = Team('yellow')
    teams = (cy_team, ye_team)
    board.reset_game()
    cy_team, ye_team = board.initialize_squares(teams)
    teams = update_team_threat(teams, board)

    return teams, board

def run_game():
    cy_team = Team('cyan')
    ye_team = Team('yellow')
    teams = (cy_team, ye_team)
    win = False
    i = 0

    cy_team, ye_team = board.initialize_squares(teams)
    
    teams = update_team_threat(teams, board)

    while win is not True:
        print()
        board.print_board()
        print()
        team = teams[i%2]
        oppo_team = teams[(i+1)%2]
        curr_teams = (team, oppo_team)
        
        move_result, curr_pos, tar_pos = player_move(curr_teams[0], curr_teams[1])
        i += act_on_result(move_result, curr_pos, tar_pos, curr_teams[0])

        if move_result in ('take', 'move', 'kingside_castle', 'queenside_castle'):
            curr_teams = update_team_threat(curr_teams, board)
            for piece in curr_teams[0].pieces:
                print('{}: {}'.format(piece, piece.threatening))
            win = checkmate(curr_teams[0], curr_teams[1], board.squares, board)

            if move_result == 'take':
                # add taken piece to opposing team's graveyard
                curr_teams[1].graveyard.append(board.squares[tar_pos])

    print('game over') 
        
        