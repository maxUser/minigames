from pieces import Piece
from board import Board
from teams import Team

from termcolor import colored

board = Board()
wh_team = Team('wh')
bl_team = Team('bl')


def check_move(team, new_x_y):
    curr_team = team.colour

    # friendly fire
    for pieces in team.army:
        # pawns, rooks, knights, bishops, king, queen
        for piece in team.army[pieces]:
            # print(piece)
            # check every piece on same team
            if piece.pos == new_x_y:
                return 'ff'

    if curr_team == 'wh':
        oppo_team = bl_team
    elif curr_team == 'bl':
        oppo_team = wh_team

    for piece_list in oppo_team.army.values():
        for piece in piece_list:
            # print(piece.pos, new_x_y)
            if piece.pos == new_x_y:
                return 'take'


    return 'good'

def y_flip(y):
    y = int(y)
    if y == 1:
        return 7
        # return 0
    elif y == 2:
        return 6
        # return 1
    elif y == 3:
        return 5
        # return 2
    elif y == 4:
        return 4
        # return 3
    elif y == 5:
        return 3
        # return 4
    elif y == 6:
        return 2
        # return 5
    elif y == 7:
        return 1
        # return 6
    elif y == 8:
        return 0
        # return 7

def letter_to_number(c):
    c = c.lower()
    if c == 'a':
        return 0
        # return 7
    elif c == 'b':
        return 1
        # return 6
    elif c == 'c':
        return 2
        # return 5
    elif c == 'd':
        return 3
        # return 4
    elif c == 'e':
        return 4
        # return 3
    elif c == 'f':
        return 5
        # return 2
    elif c == 'g':
        return 6
        # return 1
    elif c == 'h':
        return 7
        # return 0

def print_pieces(team):
    for value in team.army.values():
        for piece in value:
            print(piece)

def player_move(team):
    """
    old_pos, new_pos (str): get player input - this will be
                            in the form: [letter][number]
                            corresponding to the square on a
                            chess board.

    """
    old_pos = 'c7'# input('Piece to move: ')
    new_pos = 'e2'#input('Move to: ')

    # convert user input to list element indices
    old_x_y = [letter_to_number(old_pos[0]), y_flip(old_pos[1])]
    new_x_y = [letter_to_number(new_pos[0]), y_flip(new_pos[1])]
    print('from: ', old_x_y)
    print('to: ', new_x_y)
    print('from square: ', board.square(old_x_y))
    print('to square: ', board.square(new_x_y))


    # Check if new pos is taken by piece from same team
    result = check_move(team, new_x_y)
    if result == 'ff':
        print('Cannot move piece onto square occupied by piece of same team')
        # player_move(team)

    elif result == 'take':
        print('Taking piece at: ' + new_pos)
        board.alter(old_x_y, new_x_y)

    elif result == 'good':
        print('Moving {} to {}'.format(old_pos, new_pos))
        board.alter(old_x_y, new_x_y)



def main():

    wh_team.recruit()
    bl_team.recruit()

    # print_pieces(bl_team.army)

    # for i in range(3):
    player_move(bl_team)

    board.print()

if __name__ == '__main__':
    main()
