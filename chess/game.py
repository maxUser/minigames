from pieces import Piece
from board import Board
from teams import Team

from termcolor import colored


board = Board()
ye_team = Team('yellow')
cy_team = Team('cyan')

def king_rules(curr_pos, tar_pos):
    curr_x_y = [letter_to_number(curr_pos[0]), y_flip(curr_pos[1])]
    tar_x_y = [letter_to_number(tar_pos[0]), y_flip(tar_pos[1])]

    if abs(curr_x_y[0] - tar_x_y[0]) != 1 or abs(curr_x_y[1] - tar_x_y[1]) != 1:
        return 'illegal'

    return None

def bishop_rules(curr_pos, tar_pos):
    # Can only move diagonally
    if curr_pos[0] == tar_pos[0] or curr_pos[1] == tar_pos[1]:
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
    # curr_x_y = [letter_to_number(curr_pos[0]), y_flip(curr_pos[1])]
    # tar_x_y = [letter_to_number(tar_pos[0]), y_flip(tar_pos[1])]

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
        if curr_x_y[1] - tar_x_y[1] > 1 and colour == 'cyan':
            return 'illegal'
        elif curr_x_y[1] - tar_x_y[1] < -1 and colour == 'yellow':
            return 'illegal'
    elif board.squares[curr_pos].initial_pos:
        if curr_x_y[1] - tar_x_y[1] > 2 and colour == 'cyan':
            return 'illegal'
        elif curr_x_y[1] - tar_x_y[1] < -2 and colour == 'yellow':
            return 'illegal'

    # Take piece diagonally
    if tar_x_y[0] != curr_x_y[0] and board.squares[tar_pos] != '' and curr_x_y[1] - tar_x_y[1] == 1 and colour == 'cyan':
        return 'take'
    elif tar_x_y[0] != curr_x_y[0] and board.squares[tar_pos] != '' and curr_x_y[1] - tar_x_y[1] == -1 and colour == 'yellow':
        return 'take'

    return None

def check_move(team, curr_pos, tar_pos, curr_x_y, tar_x_y):
    """
    The logic: check if move is illegal, if not determine
                whether it is a take or move.
    """

    colour = team.colour
    oppo_team = get_oppo_team(colour)
    result = 'no_result'

    # check if input matches a valid board square
    if curr_pos not in board.squares or tar_pos not in board.squares:
        return 'invalid_input'

    # player selected empty square or player trying to move wrong team
    if board.squares[curr_pos] == '' or colour != board.squares[curr_pos].team:
        return 'selection_error'

    # friendly fire is off
    if board.squares[curr_pos] != '' and board.squares[tar_pos] != '':
        if board.squares[tar_pos].team == board.squares[curr_pos].team:
            return 'ff'

    # check if piece move through another piece (unless knight)
    # IMPROVE: there must be simpler way to do this
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
            # print(start, end)
            if curr_pos[1] == tar_pos[1] and colour == 'cyan':
                # same y
                if start < end:
                    # left to right
                    for i in range(start+1, end):
                        pos = str(number_to_letter(i)+curr_pos[1])
                        print(pos)
                        if board.squares[pos] != '':
                            return 'illegal'
                else:
                    # right to left
                    for i in range(end, start-1):
                        pos = str(number_to_letter(i)+curr_pos[1])
                        print(pos)
                        if board.squares[pos] != '':
                            return 'illegal'
            elif curr_pos[1] == tar_pos[1] and colour == 'yellow':
                # same y
                if start < end:
                    # left to right
                    for i in range(start+1, end):
                        pos = str(number_to_letter(i)+curr_pos[1])
                        print(pos)
                        if board.squares[pos] != '':
                            return 'illegal'
                else:
                    # right to left
                    for i in range(end, start-1):
                        pos = str(number_to_letter(i)+curr_pos[1])
                        print(pos)
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
        result = king_rules(curr_pos, tar_pos)

    if result == 'illegal':
        return result
    else:
        # move or take
        if board.squares[tar_pos] != '':
            return 'move'
        else:
            return 'take'

def y_flip(y):
    y = int(y)
    if y == 1:
        return 7
    elif y == 2:
        return 6
    elif y == 3:
        return 5
    elif y == 4:
        return 4
    elif y == 5:
        return 3
    elif y == 6:
        return 2
    elif y == 7:
        return 1
    elif y == 8:
        return 0

def letter_to_number(c):
    c = c.lower()
    if c == 'a':
        return 0
    elif c == 'b':
        return 1
    elif c == 'c':
        return 2
    elif c == 'd':
        return 3
    elif c == 'e':
        return 4
    elif c == 'f':
        return 5
    elif c == 'g':
        return 6
    elif c == 'h':
        return 7

def number_to_letter(n):
    if n == 0:
        return 'a'
    elif n == 1:
        return 'b'
    elif n == 2:
        return 'c'
    elif n == 3:
        return 'd'
    elif n == 4:
        return 'e'
    elif n == 5:
        return 'f'
    elif n == 6:
        return 'g'
    elif n == 7:
        return 'h'

def get_oppo_team(curr_team):
    if curr_team == 'cyan':
        return ye_team
    elif curr_team == 'yellow':
        return cy_team

def print_error(msg):
    print('ERROR:\n***\n{}\n***'.format(msg))

def get_piece_to_move():
    return input('Piece to move: ')

def get_target_position():
    return input('Move to: ')

def player_move(team):
    """
    curr_pos, tar_pos (str): get player input - this will be
                            in the form: [letter][number]
                            corresponding to the square on a
                            chess board.

    """

    print(colored(team.colour + '\'s turn', team.colour))

    curr_pos = get_piece_to_move()#input('Piece to move: ')
    tar_pos = get_target_position()#input('Move to: ')

    if curr_pos == 'pp':
        print_pieces(cy_team)
        print_pieces(ye_team)

    # convert user input to list element indices
    curr_x_y = [letter_to_number(curr_pos[0]), y_flip(curr_pos[1])]
    tar_x_y = [letter_to_number(tar_pos[0]), y_flip(tar_pos[1])]


    # print('From {}'.format(curr_x_y))
    # print('To {}'.format(tar_x_y))
    result = check_move(team, curr_pos, tar_pos, curr_x_y, tar_x_y)
    # print('result of check_move is: {}'.format(result))

    return result, curr_pos, tar_pos, curr_x_y, tar_x_y

def act_on_result(result, curr_pos, tar_pos, curr_x_y, tar_x_y, team):
    """
        Takes result of player_move and check_move functions
        to determine next action

        Return: 0 if move is invalid (same player's turn)
                1 if move is valid (next player's turn)
    """
    # print('result is {}'.format(result))
    if result == 'ff':
        print_error('Target square occupied by friendly piece')
        # player_move(team)
        return 0

    elif result == 'illegal':
        print_error('Illegal move')
        # player_move(team)
        return 0

    elif result == 'selection_error':
        print_error('{} is an invalid selection'.format(curr_pos))
        # player_move(team)
        return 0

    elif result == 'invalid_input':
        print_error('Invalid input')
        # player_move(team)
        return 0

    elif result == 'take':
        print('Taking piece at: ' + tar_pos)
        board.alter(curr_x_y, tar_x_y)

        # add piece to team's graveyard
        team.graveyard.append(board.squares[tar_pos])
        # remove current piece occupying square
        board.squares[tar_pos] = board.squares[curr_pos]
        board.squares[curr_pos] = ''
        return 1

    elif result == 'move':
        print('Moving {} to {}'.format(curr_pos, tar_pos))
        board.squares[curr_pos].initial_pos = False
        board.alter(curr_x_y, tar_x_y)
        board.move_piece(curr_pos, tar_pos)
        return 1

def main():

    teams = (cy_team, ye_team)

    win = False
    i = 0

    board.initialize_squares()
    # board.print_board()
    # board.reset_game()
    # board.print_board()
    # pawn = board.squares['a2']
    # print('as', pawn)
    # return None


    while win is False:
        print()
        # print('ROUND {}'.format(i+1))
        # print('i: {}'.format(i))
        board.print_board()

        team = teams[i%2]
        move_result, curr_pos, tar_pos, curr_x_y, tar_x_y = player_move(team)
        i += act_on_result(move_result, curr_pos, tar_pos, curr_x_y, tar_x_y, team)


if __name__ == '__main__':
    main()
