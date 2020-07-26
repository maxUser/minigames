from pieces import Piece
from board import Board
from teams import Team

from termcolor import colored

board = Board()


def check_take(team, new_x_y):
    print(team)

    return False

def check_ff(team, new_x_y):
    for pieces in team:
        # pawns, rooks, knights, bishops, king, queen
        for piece in team[pieces]:
            # check every piece on same team
            if piece.pos == new_x_y:
                return True
    return False

def x_flip(x):
    x = int(x)
    if x == 1:
        return 7
    elif x == 2:
        return 6
    elif x == 3:
        return 5
    elif x == 4:
        return 4
    elif x == 5:
        return 3
    elif x == 6:
        return 2
    elif x == 7:
        return 1
    elif x == 8:
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

def print_pieces(teams, piece=''):
    if piece == '':
        for team in teams:
            for key, value in teams[team].items():
                for item in value:
                    print(item)
    else:
        for team in teams:
            for p in teams[team][piece]:
                print(p)

def player_move(team):
    # eg. d4
    old_pos = 'a2'# input('Piece to move: ')
    new_pos = 'a3'#input('Move to: ')

    old_x_y = [x_flip(old_pos[1]), letter_to_number(old_pos[0])]
    new_x_y = [x_flip(new_pos[1]), letter_to_number(new_pos[0])]

    # Check if new pos is taken by piece from same team
    bad_move = check_ff(team, new_x_y) # ff = friendly fire
    if bad_move is False:
        board.alter(old_x_y, new_x_y)
    else:
        print('bad move, try again')
        player_move(team)


    # Check if new pos is taken by piece from opponent
    take_piece = check_take(team, new_x_y)

    print(take_piece)




def main():
    team = Team('wh')
    print(team.army)
    team.populate()
    # for i in range(3):
    player_move(team.army)
    # print_pieces(teams.teams)

    # board.print()

if __name__ == '__main__':
    main()
