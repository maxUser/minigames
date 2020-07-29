from pieces import Piece
from board import Board
from teams import Team

from termcolor import colored

board = Board()
ye_team = Team('yellow')
cy_team = Team('cyan')

def get_oppo_team(curr_team):
    if curr_team == 'cyan':
        return ye_team
    elif curr_team == 'yellow':
        return cy_team

def check_move(team, old_x_y, new_x_y):
    colour = team.colour
    oppo_team = get_oppo_team(colour)

    # friendly fire
    for pieces in team.army:
        # pawns, rooks, knights, bishops, king, queen
        for piece in team.army[pieces]:
            # check every piece on same team
            if piece.pos == new_x_y:
                return 'ff'

    # take opponent's piece
    for piece_list in oppo_team.army.values():
        for piece in piece_list:
            # print(piece.pos, new_x_y)
            if piece.pos == new_x_y:
                return 'take'

    # trying to move wrong team
    for piece_list in oppo_team.army.values():
        for piece in piece_list:
            # find piece selected to be moved
            if piece.pos == old_x_y:
                # determine if piece is on same team as player moving it
                if team.colour != piece.team:
                    return 'team_error'



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
    board.print()

    print(team.colour + ' turn')
    old_pos = input('Piece to move: ')
    new_pos = input('Move to: ')

    if old_pos == 'pp':
        print_pieces(cy_team)
        print_pieces(ye_team)

    # convert user input to list element indices
    old_x_y = [letter_to_number(old_pos[0]), y_flip(old_pos[1])]
    new_x_y = [letter_to_number(new_pos[0]), y_flip(new_pos[1])]
    # print('from: ', old_x_y)
    # print('to: ', new_x_y)
    # print('from square: ', board.square(old_x_y))
    # print('to square: ', board.square(new_x_y))

    piece_to_move = team.get_piece_by_pos(old_x_y)

    # Check if new pos is taken by piece from same team
    result = check_move(team, old_x_y, new_x_y)
    try:
        if result == 'ff':
            print('ERROR:\n***\nCannot move piece onto square occupied\nby piece of same team\n***')
            player_move(team)


        elif result == 'team_error':
            print('ERROR:\n***\nCannot move opponent\'s pieces\n***')
            player_move(team)


        elif result == 'take':
            print('Taking piece at: ' + new_pos)
            board.alter(old_x_y, new_x_y)

            # remove current piece occupying square
            piece_to_remove = get_oppo_team(team.colour).get_piece_by_pos(new_x_y)
            piece_to_remove.move([-1, -1])

            # move piece taking its place
            piece_to_move.move(new_x_y)


        elif result == 'move':
            print('Moving {} to {}'.format(old_pos, new_pos))
            board.alter(old_x_y, new_x_y)
            piece_to_move.move(new_x_y)

    except AttributeError:
        print('It is not {}\'s turn'.format(team.colour))
        player_move(team)


    return False

def main():

    cy_team.recruit()
    ye_team.recruit()
    # print_pieces(ye_team)

    teams = (cy_team, ye_team)

    win = False
    i = 0
    while win is False:
        print()
        win = player_move(teams[i%2])
        i += 1


if __name__ == '__main__':
    main()
