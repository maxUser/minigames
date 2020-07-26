from pieces import Piece
from board import Board

from termcolor import colored


board = Board()

def check_move(team, new_x_y):
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

def print_pieces(teams, piece):
    for team in teams:
        for p in teams[team][piece]:
            print(p)


def player_move(team):
    # eg. d4
    old_pos = 'a8'# input('Piece to move: ')
    new_pos = 'h8'#input('Move to: ')

    old_x_y = [x_flip(old_pos[1]), letter_to_number(old_pos[0])]
    new_x_y = [x_flip(new_pos[1]), letter_to_number(new_pos[0])]

    # Check if new pos is taken by piece from same team
    bad_move = check_move(team, new_x_y)
    if bad_move is False:
        board.alter(old_x_y, new_x_y)

    else:
        print('bad move, try again')
        player_move(team)


def starting_pos(type, team, i):
    #   0 1 2 3 4 5 6 7
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7

    if team == 'wh':
        if type == 'pawn':
            return [i, 1]
        elif type == 'rook':
            return [0, 7], [7, 7]
        elif type == 'knight':
            return [1, 7], [6, 7]
        elif type == 'bishop':
            return [2, 7], [5, 7]
    elif team == 'bl':
        if type == 'pawn':
            return [i, 6]
        elif type == 'rook':
            return [0, 0], [0, 7]
        elif type == 'knight':
            return [0, 1], [0, 6]
        elif type == 'bishop':
            return [0, 2], [0, 5]

def populate():
    teams = {
        'wh':{'pawns':[], 'rooks':[], 'knights':[], 'bishops':[], 'king':[], 'queen':[]},
        'bl':{'pawns':[], 'rooks':[], 'knights':[], 'bishops':[], 'king':[], 'queen':[]}
        }

    for team in teams:
        # pawns
        for i in range(8):
            type = 'pawn'
            t_pawn = Piece(type, team, starting_pos(type, team, i))
            teams[team]['pawns'].append(t_pawn)

        #rooks, knights, bishops
        types = ['rook', 'knight', 'bishop']
        for type in types:
            piece_pos1, piece_pos2 = starting_pos(type, team, -1)
            piece1 = Piece(type, team, piece_pos1)
            piece2 = Piece(type, team, piece_pos2)
            if type == 'rook':
                teams[team]['rooks'].append(piece1)
                teams[team]['rooks'].append(piece2)
            elif type == 'knight':
                teams[team]['knights'].append(piece1)
                teams[team]['knights'].append(piece2)
            elif type == 'bishop':
                teams[team]['bishops'].append(piece1)
                teams[team]['bishops'].append(piece2)

    return teams


def main():
    teams = populate()
    # for i in range(3):
    # player_move(teams['wh'])
    print_pieces(teams, 'knights')

    board.print()

if __name__ == '__main__':
    main()
