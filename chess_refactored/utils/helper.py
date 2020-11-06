from utils.piece_rules import (queen_rules, king_rules, bishop_rules,
                        knight_rules, rook_rules, pawn_rules)

def move_or_take(board, piece, target):
    return None

def check_move_legality(board, piece, target):
    legal = True
    # check if empty square selected
    if piece is None:
        return False
    # check if target square exists
    if target not in board.squares:
        return False
    # check if target square contains friendly piece
    if board.squares[target]:
        if board.squares[target].team == piece.team:
            return False
    # check piece-specific rules
    result = True
    if piece.type == 'pawn':
        result = pawn_rules(board, piece, target)
    elif piece.type == 'rook':
        result = rook_rules(piece, target)
    elif piece.type == 'knight':
        result = knight_rules(piece, target)
    elif piece.type == 'bishop':
        result = bishop_rules(piece, target)
    # elif piece.type == 'king':
    #     result = king_rules()
    # elif piece.type == 'queen':
    #     result = queen_rules()
    if result is False:
        return False

    # check if piece move through another piece unless knight
    if piece.type != 'knight':
        for square in get_between_exclusive(piece.pos, target):
            if board.squares[square] is not None:
                return False
    return legal

def get_between_exclusive(start, end):
    """ Return list of all squares between start and end exclusive

        Args
            start (str): a board position, eg. 'a2'
            end (str): a board position, eg. 'a4'
    """
    start = str(letter_to_number(start[0])) + start[1]
    end = str(letter_to_number(end[0])) + end[1]
    startX = int(start[0])
    startY = int(start[1])
    endX = int(end[0])
    endY = int(end[1])
    x_diff = []
    y_diff = []
    if startX != endX and startY != endY:
        # diagonal
        if startX < endX:
            # Left to right
            for i in range(startX+1, endX):
                x_diff.append(i)
        elif startX > endX:
            # Right to left
            for i in range(startX-1, endX, -1):
                x_diff.append(i)
        if startY < endY:
            # Down to up
            for i in range(startY+1, endY):
                y_diff.append(i)
        elif startY > endY:
            # Up to down
            for i in range(startY-1, endY, -1):
                y_diff.append(i)
    elif startX == endX and startY != endY:
        # x threat
        if startY < endY:
            for i in range(startY+1, endY):
                y_diff.append(i)
        elif startY > endY:
            for i in range(startY-1, endY, -1):
                y_diff.append(i)
        for i in range(len(y_diff)):
            x_diff.append(startX)
    elif startY == endY and startX != endX:
        # y threat
        if startX < endX:
            for i in range(startX+1, endX):
                x_diff.append(i)
        elif startX > endX:
            for i in range(startX-1, endX, -1):
                x_diff.append(i)
        for i in range(len(x_diff)):
            y_diff.append(startY)

    return [number_to_letter(i)+str(j) for i, j in zip(x_diff, y_diff)]

def get_piece_to_move(square, team):
    """ Find piece on team given a square
    
    Args:
        square (str) - the coordinates for a square on the board (e.g. 'a2')
        team (obj) - the team making the move
    Returns:
        A piece object occupied by the given square
    """
    for piece in team.pieces:
        if piece.pos == square:
            return piece

def letter_to_number(char):
    if char == 'a':
        return 1
    elif char == 'b':
        return 2
    elif char == 'c':
        return 3
    elif char == 'd':
        return 4
    elif char == 'e':
        return 5
    elif char == 'f':
        return 6
    elif char == 'g':
        return 7
    elif char == 'h':
        return 8

def number_to_letter(num):
    if num == 1:
        return 'a'
    elif num == 2:
        return 'b'
    elif num == 3:
        return 'c'
    elif num == 4:
        return 'd'
    elif num == 5:
        return 'e'
    elif num == 6:
        return 'f'
    elif num == 7:
        return 'g'
    elif num == 8:
        return 'h'

def piece_to_move_prompt():
    return input('Piece to move: ')

def target_square_prompt():
    return input('Move to: ')
