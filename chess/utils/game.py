from utils.pieces import Piece
from utils.board import Board
from utils.teams import Team
from termcolor import colored
from utils.helper import (y_flip, get_x_between, get_y_between,
                          letter_to_number, number_to_letter,
                          print_error, get_piece_to_move,
                          get_target_position, update_team_threat)




board = Board()

def queen_rules(curr_pos, tar_pos):
    curr_x_y = [letter_to_number(curr_pos[0]), y_flip(curr_pos[1])]
    tar_x_y = [letter_to_number(tar_pos[0]), y_flip(tar_pos[1])]

    if curr_pos[0] != tar_pos[0] and curr_pos[1] != tar_pos[1]:
        # Non-straight movement
        if abs(curr_x_y[0] - tar_x_y[0]) - abs(curr_x_y[1] - tar_x_y[1]) != 0:
            # disallow awkward moves like E3 to F5
            return 'illegal'

    return None

def king_rules(team, oppo_team, curr_pos, tar_pos):
    curr_x_y = [letter_to_number(curr_pos[0]), y_flip(curr_pos[1])]
    tar_x_y = [letter_to_number(tar_pos[0]), y_flip(tar_pos[1])]


    kingside_rook = board.squares[number_to_letter(curr_x_y[0]+3) + str(curr_pos[1])]
    queenside_rook = board.squares[number_to_letter(curr_x_y[0]-4) + str(curr_pos[1])]
    king = board.squares[curr_pos]

    # Castling
    # 1. The castling must be kingside or queenside.
    # 2. Neither the king nor the chosen rook has previously moved.
    # 3. There are no pieces between the king and the chosen rook.
    # 4. The king is not currently in check.
    # 5. The king does not pass through a square that is attacked by an enemy piece.
    # 6. The king does not end up in check. (True of any legal move.)
    if (tar_x_y[0] == curr_x_y[0] + 2 # 1. Kingside castle
        and (king.initial_pos is True and kingside_rook.initial_pos is True) # 2. Neither the king nor the chosen rook has previously moved.
        and (not board.squares[tar_pos] and not board.squares[number_to_letter(curr_x_y[0]+1) + curr_pos[1]]) # 3. There are no pieces between the king and the chosen rook. 
        and curr_pos not in oppo_team.threatening # 4. The king is not currently in check.
        and str(number_to_letter(curr_x_y[0]+1) + curr_pos[1]) not in oppo_team.threatening # 5. The king does not pass through a square that is attacked by an enemy piece.
        and str(number_to_letter(curr_x_y[0]+2) + curr_pos[1]) not in oppo_team.threatening): # 6. The king does not end up in check. (True of any legal move.)
        
        return 'kingside_castle'  

    elif (tar_x_y[0] == curr_x_y[0] - 2
        and king.initial_pos is True and queenside_rook.initial_pos is True
        and not board.squares[tar_pos] and not board.squares[number_to_letter(curr_x_y[0]-1) + curr_pos[1]]
        and curr_pos not in oppo_team.threatening
        and str(number_to_letter(curr_x_y[0]-1) + curr_pos[1]) not in oppo_team.threatening
        and str(number_to_letter(curr_x_y[0]-2) + curr_pos[1]) not in oppo_team.threatening):
        
        return 'queenside_castle'

    elif abs(curr_x_y[0] - tar_x_y[0]) > 1 or abs(curr_x_y[1] - tar_x_y[1]) > 1:
        # moving king more than 1 square
        return 'illegal'

    elif (tar_x_y[0] == curr_x_y[0] + 2 
        and (king.initial_pos is False or kingside_rook.initial_pos is False
        or board.squares[number_to_letter(curr_x_y[0]+1) + curr_pos[1]]
        or curr_pos in oppo_team.threatening
        or str(number_to_letter(curr_x_y[0]+1) + curr_pos[1]) in oppo_team.threatening
        or str(number_to_letter(curr_x_y[0]+2) + curr_pos[1]) in oppo_team.threatening)):
        # Kingside castle fail
        return 'illegal'

    elif (tar_x_y[0] == curr_x_y[0] - 2 
        and (king.initial_pos is False or queenside_rook.initial_pos is False
        or board.squares[number_to_letter(curr_x_y[0]-1) + curr_pos[1]]
        or curr_pos in oppo_team.threatening
        or str(number_to_letter(curr_x_y[0]-1) + curr_pos[1]) in oppo_team.threatening
        or str(number_to_letter(curr_x_y[0]-2) + curr_pos[1]) in oppo_team.threatening)):
        # queenside castle fail
        return 'illegal'
    

    return None

def bishop_rules(curr_pos, tar_pos):
    curr_x_y = [letter_to_number(curr_pos[0]), y_flip(curr_pos[1])]
    tar_x_y = [letter_to_number(tar_pos[0]), y_flip(tar_pos[1])]

    # Can only move diagonally
    # Difference in x == difference in y
    if curr_pos[0] == tar_pos[0] or curr_pos[1] == tar_pos[1]:
        # disallow straight or lateral movement
        return 'illegal'

    if abs(curr_x_y[0] - tar_x_y[0]) - abs(curr_x_y[1] - tar_x_y[1]) != 0:
        # disallow awkward moves like E3 to F5
        return 'illegal'

    return None

def knight_rules(curr_pos, tar_pos):
    """
        Knights can only move in an L shape.
        Ensure the tar_pos is +-2 x or y and
        +- 1 x or y.
        Example scenarios (Cyan):
        1) Move up (y-2) and left (x-1)
        2) Move right (x+2) and up (y-1)
        3) Move down (y+2) and left (x-1)
        x operators are swapped for yellow
    """
    curr_x_y = [letter_to_number(curr_pos[0]), y_flip(curr_pos[1])]
    tar_x_y = [letter_to_number(tar_pos[0]), y_flip(tar_pos[1])]

    if abs(curr_x_y[0] - tar_x_y[0]) == 1:
        # up or down move
        if abs(curr_x_y[1] - tar_x_y[1]) != 2:
            # diff in y must == 2
            return 'illegal'
    elif abs(curr_x_y[1] - tar_x_y[1]) == 1:
        # lateral move
        if abs(curr_x_y[0] - tar_x_y[0]) != 2:
            # diff in y must == 2
            return 'illegal'
    else:
        return 'illegal'

    return None

def rook_rules(curr_pos, tar_pos):
    # Cannot move diagonally
    if curr_pos[0] != tar_pos[0] and curr_pos[1] != tar_pos[1]:
        return 'illegal'

    return None

def pawn_rules(colour, curr_pos, tar_pos):
    curr_x_y = [letter_to_number(curr_pos[0]), y_flip(curr_pos[1])]
    tar_x_y = [letter_to_number(tar_pos[0]), y_flip(tar_pos[1])]

    # Cannot move backwards
    if curr_x_y[1] - tar_x_y[1] <= 0 and colour == 'cyan':
        return 'illegal'
    if curr_x_y[1] - tar_x_y[1] >= 0 and colour == 'yellow':
        return 'illegal'

    # Cannot take piece with same x value
    if tar_x_y[0] == curr_x_y[0] and board.squares[tar_pos] != '':
        return 'illegal'

    # Cannot move diagonally
    if board.squares[tar_pos] == '' and tar_x_y[0] != curr_x_y[0]:
        return 'illegal'

    # Can only move forward by 1 square unless moving from
    # starting position, then can move 1 or 2 squares forward
    if not board.squares[curr_pos].initial_pos:
        if abs(curr_x_y[1] - tar_x_y[1]) != 1:
            return 'illegal'
    elif board.squares[curr_pos].initial_pos:
        if abs(curr_x_y[1] - tar_x_y[1]) > 2:
            return 'illegal'

    # Take piece diagonally
    if tar_x_y[0] != curr_x_y[0] and board.squares[tar_pos] != '' and curr_x_y[1] - tar_x_y[1] == 1 and colour == 'cyan':
        return 'take'
    elif tar_x_y[0] != curr_x_y[0] and board.squares[tar_pos] != '' and curr_x_y[1] - tar_x_y[1] == -1 and colour == 'yellow':
        return 'take'

    return None

def check_move(team, oppo_team, curr_pos, tar_pos, curr_x_y, tar_x_y):
    """
    The logic: check if move is illegal, if not determine
               whether it is a take or move action.
    """
    colour = team.colour
    result = 'no_result'

    # check if input matches a valid board square
    if curr_pos not in board.squares or tar_pos not in board.squares:
        return 'invalid_input'

    # player selected empty square or player trying to move wrong team
    if board.squares[curr_pos] == '' or colour != board.squares[curr_pos].team.colour:
        return 'selection_error'

    # friendly fire is off
    if board.squares[curr_pos] != '' and board.squares[tar_pos] != '':
        if board.squares[tar_pos].team == board.squares[curr_pos].team:
            return 'ff'

    # check if piece move through another piece (unless knight)
    # TODO: there must be simpler way to do this - at least put it in helper.py
    if board.squares[curr_pos].type != 'knight':
        exes = []
        whys = []

        # get all in between squares
        if abs((tar_x_y[0]-curr_x_y[0])) == abs((tar_x_y[1]-curr_x_y[1])):
            # diagonal move
            if curr_x_y[0] > tar_x_y[0]:
                # left diagonal
                for x in range(tar_x_y[0]+1, curr_x_y[0]):
                    exes.append(x)
            else:
                # right diagonal
                for x in range(curr_x_y[0]+1, tar_x_y[0]):
                    exes.append(x)

            if curr_x_y[1] > tar_x_y[1]:
                # upward diagonal
                for y in range(tar_x_y[1]+1, curr_x_y[1]):
                    whys.append(y)
            else:
                # downward diagonal
                for y in range(curr_x_y[1]+1, tar_x_y[1]):
                    whys.append(y)
        else:
            # straight move
            if curr_pos[0] == tar_pos[0] and colour == 'cyan':
                # same x
                for i in range(int(curr_pos[1])+1, int(tar_pos[1])):
                    pos = curr_pos[0] + str(i)
                    if board.squares[pos] != '':
                        result = 'illegal'
            elif curr_pos[0] == tar_pos[0] and colour == 'yellow':
                # same x
                for i in range(int(tar_pos[1])+1, int(curr_pos[1])):
                    pos = curr_pos[0] + str(i)
                    if board.squares[pos] != '':
                        return 'illegal'
            # lateral move
            start = letter_to_number(curr_pos[0])
            end = letter_to_number(tar_pos[0])
            if curr_pos[1] == tar_pos[1] and colour == 'cyan':
                # same y
                if start < end:
                    # left to right
                    for i in range(start+1, end):
                        pos = str(number_to_letter(i)+curr_pos[1])
                        # print(pos)
                        if board.squares[pos] != '':
                            return 'illegal'
                else:
                    # right to left
                    for i in range(end, start-1):
                        pos = str(number_to_letter(i)+curr_pos[1])
                        # print(pos)
                        if board.squares[pos] != '':
                            return 'illegal'
            elif curr_pos[1] == tar_pos[1] and colour == 'yellow':
                # same y
                if start < end:
                    # left to right
                    for i in range(start+1, end):
                        pos = str(number_to_letter(i)+curr_pos[1])
                        # print(pos)
                        if board.squares[pos] != '':
                            return 'illegal'
                else:
                    # right to left
                    for i in range(end, start-1):
                        pos = str(number_to_letter(i)+curr_pos[1])
                        # print(pos)
                        if board.squares[pos] != '':
                            return 'illegal'

    # check if move is legal according to piece move restrictions
    if board.squares[curr_pos].type == 'pawn':
        result = pawn_rules(colour, curr_pos, tar_pos)
    elif board.squares[curr_pos].type == 'rook':
        result = rook_rules(curr_pos, tar_pos)
    elif board.squares[curr_pos].type == 'knight':
        result = knight_rules(curr_pos, tar_pos)
    elif board.squares[curr_pos].type == 'bishop':
        result = bishop_rules(curr_pos, tar_pos)
    elif board.squares[curr_pos].type == 'king':
        result = king_rules(team, oppo_team, curr_pos, tar_pos)
    elif board.squares[curr_pos].type == 'queen':
        result = queen_rules(curr_pos, tar_pos)

    if result in ('kingside_castle', 'queenside_castle', 'illegal') :
        return result
    else:
        if not board.squares[tar_pos]:
            return 'move'
        else:
            return 'take'

def player_move(team, oppo_team):
    print(colored(team.colour + '\'s turn', team.colour))

    curr_pos = get_piece_to_move()
    tar_pos = get_target_position()

    # convert user input to list element indices
    curr_x_y = [letter_to_number(curr_pos[0]), y_flip(curr_pos[1])]
    tar_x_y = [letter_to_number(tar_pos[0]), y_flip(tar_pos[1])]

    result = check_move(team, oppo_team, curr_pos, tar_pos, curr_x_y, tar_x_y)

    return result, curr_pos, tar_pos, curr_x_y, tar_x_y

def act_on_result(result, curr_pos, tar_pos, curr_x_y, tar_x_y, team):
    """ 
        Takes result of player_move and check_move functions
        to determine next action

        Return: 0 if move is invalid (same player's turn)
                1 if move is valid (next player's turn)
    """
    #print('Result: {}'.format(result))
    if result == 'ff':
        print_error('Target square occupied by friendly piece')
        return 0

    elif result == 'illegal':
        print_error('Illegal move')
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

    while win is False:
        print()
        board.print_board()
        print()
        team = teams[i%2]
        oppo_team = teams[(i+1)%2]

        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(team, oppo_team)
        
        if move_result == 'take':
            # add taken piece to opposing team's graveyard
            oppo_team.graveyard.append(board.squares[tar_pos])
            # update threat
            teams = update_team_threat(teams, board)       
        elif move_result in ('move', 'kingside_castle', 'queenside_castle'):
            # update threat
            teams = update_team_threat(teams, board)

        i += act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, team)
        
        
        