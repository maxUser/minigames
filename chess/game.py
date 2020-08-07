from pieces import Piece
from board import Board
from teams import Team

from termcolor import colored


board = Board()
ye_team = Team('yellow')
cy_team = Team('cyan')


def rook_rules(colour, curr_pos, tar_pos):
    curr_x_y = [letter_to_number(curr_pos[0]), y_flip(curr_pos[1])]
    tar_x_y = [letter_to_number(tar_pos[0]), y_flip(tar_pos[1])]

    # Cannot move diagonally
    if curr_x_y[0] != tar_x_y[0] or curr_x_y[1] != tar_x_y[1]:
        return 'illegal'

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


    return 'move'

def check_move(team, curr_pos, tar_pos, curr_x_y, tar_x_y):
    colour = team.colour
    oppo_team = get_oppo_team(colour)

    # check if input matches a valid board square
    if curr_pos not in board.squares or tar_pos not in board.squares:
        return 'invalid_input'

    # player selected empty square or player trying to move wrong team
    if board.squares[curr_pos] == '' or colour != board.squares[curr_pos].team:
        return 'selection_error'

    # check if move is legal according to piece move restrictions
    if board.squares[curr_pos].type == 'pawn':
        return pawn_rules(colour, curr_pos, tar_pos)

    # friendly fire is off
    if board.squares[curr_pos] != '' and board.squares[tar_pos] != '':
        if board.squares[tar_pos].team == board.squares[curr_pos].team:
            return 'ff'

    # check if piece move through another piece (unless knight)
    if board.squares[curr_pos].type != 'knight':
        exes = []
        whys = []

        # get all in between squares
        if abs((tar_x_y[0]-curr_x_y[0])) == abs((tar_x_y[1]-curr_x_y[1])):
            # diagonal move
            if curr_x_y[0] > tar_x_y[0]:
                # left diagonal
                print('left diagonal')
                for x in range(tar_x_y[0]+1, curr_x_y[0]):
                    exes.append(x)
            else:
                # right diagonal
                print('right diagonal')
                for x in range(curr_x_y[0]+1, tar_x_y[0]):
                    exes.append(x)

            if curr_x_y[1] > tar_x_y[1]:
                # upward diagonal
                print('upward diagonal')
                for y in range(tar_x_y[1]+1, curr_x_y[1]):
                    whys.append(y)

            else:
                # downward diagonal
                print('downward diagonal')
                for y in range(curr_x_y[1]+1, tar_x_y[1]):
                    whys.append(y)
        else:
            # straight move
            if curr_x_y[0] > tar_x_y[0]:
                x1 = curr_x_y[0]
                while x1 > tar_x_y[0]:
                    x1 -= 1
                    exes.append(x1)
            elif tar_x_y[0] > curr_x_y[0]:
                x2 = tar_x_y[0]
                while x2 > curr_x_y[0]:
                    x2 -= 1
                    exes.append(x2)

            elif curr_x_y[1] > tar_x_y[1]:
                y1 = curr_x_y[1]
                while y1 > tar_x_y[1]:
                    y1 -= 1
                    whys.append(y1)
            elif tar_x_y[1] > curr_x_y[1]:
                y2 = tar_x_y[1]
                while y2 > curr_x_y[1]:
                    y2 -= 1
                    whys.append(y2)

        exes = exes[::-1] # reverse list
        if not exes:
            for i in range(len(whys)):
                exes.append(0)
        if not whys:
            for i in range(len(exes)):
                whys.append(0)

        for index, value in enumerate(exes):
            # match indices of exes and whys lists to get
            # all squares between curr_pos and tar_pos
            letter = number_to_letter(value)
            number = y_flip(whys[index])
            pos = letter+str(number)
            if len(pos) == 2:
                if board.squares[pos] != '':
                    return 'illegal'

        return 'move'




    # if target sqauare is empty, move piece
    if board.squares[tar_pos] == '':
        """THIS MUST BE REMOVED
            once all piece specific rules are in place
        """
        return 'move'

def check_move_old(team, curr_x_y, new_x_y):
    colour = team.colour
    oppo_team = get_oppo_team(colour)

    # friendly fire is off
    for pieces in team.army:
        for piece in team.army[pieces]:
            if piece.pos == new_x_y:
                return 'ff'

    # player trying to move wrong team
    for piece_list in oppo_team.army.values():
        for piece in piece_list:
            if piece.pos == curr_x_y:
                if team.colour != piece.team:
                    return 'team_error'

    # Check if move is legal according to piece move restrictions
    piece_to_move = team.get_piece_by_pos(curr_x_y)
    if colour == 'cyan':
        if piece_to_move.type == 'pawn':
            if ((new_x_y == [curr_x_y[0]+1, curr_x_y[1]-1]) and (curr_x_y[0] != 7)) or ((new_x_y == [curr_x_y[0]-1, curr_x_y[1]-1]) and (curr_x_y[0] != 0)):
                # check if opponent has piece in diagonal square
                for piece_list in oppo_team.army.values():
                    for piece in piece_list:
                        pass
                print('diagonal move')
                return 'move'

            if piece_to_move.initial_pos == True:
                if (curr_x_y[1] - new_x_y[1] <= 2) and (new_x_y[0] == curr_x_y[0]):
                    pass
                else:
                    return 'illegal'
            elif piece_to_move.initial_pos == False:
                if (curr_x_y[1] - new_x_y[1] > 1) and (new_x_y[0] == curr_x_y[0]):
                    return 'illegal'
            print('here')

    elif colour == 'yellow':
        if piece_to_move.type == 'pawn':
            if piece_to_move.initial_pos == True:
                if (curr_x_y[1] - new_x_y[1] >= -2) and (new_x_y[0] == curr_x_y[0]):
                    pass
                else:
                    return 'illegal'
            elif piece_to_move.initial_pos == False:
                if (curr_x_y[1] - new_x_y[1] < -1) and (new_x_y[0] == curr_x_y[0]):
                    return 'illegal'


    # take opponent's piece
    for piece_list in oppo_team.army.values():
        for piece in piece_list:
            if piece.pos == new_x_y:
                piece.initial_pos = False
                return 'take'


    piece_to_move.initial_pos = False
    return 'move'

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
