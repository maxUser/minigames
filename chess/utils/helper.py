from utils.piece_rules import (queen_rules, king_rules, bishop_rules,
                        knight_rules, rook_rules, pawn_rules)

def checkmate(team, oppo_team, squares, board):
    """ Determine whether oppo_team has been checkmated.
        A game position in which a player's king is in check 
        (threatened with capture) and there is no way to avoid the threat.

        Args
            team = the team that just played a move
            oppo_team = the other team (being checked)
            squares = dictionary of squares on the board and what they contain
            board = 
    """
    threatening_piece = ''
    oppo_team_king_pos = [piece.pos for piece in oppo_team.pieces if piece.type == 'king'][0]

    # First, resolve check  
    if oppo_team_king_pos in team.threatening:
        print('{} is in check!'.format([piece for piece in oppo_team.pieces if piece.type == 'king'][0]))
        threatening_piece = [piece for piece in team.pieces if oppo_team_king_pos in piece.threatening][0]
    else:
        # No check
        return False, team

    threatening_piece_pos = threatening_piece.pos

    # Second, resolve possible escape from check
    # 1) can the king move to a non-threatened square
    # 2) can a piece move into the path of the threat (non-knight, non-pawn threat)
    # 3) can a piece take the threatening piece
    if threatening_piece.type in ('knight', 'pawn'):
        # nothing can move into the path of the threat posed by knights or pawns        
        if get_king_safe_moves(oppo_team_king_pos, team, squares) or is_threatened(threatening_piece_pos, oppo_team):
            # if the king has a place to move out of check, or
            # if piece checking king can be taken
            team.check = True
            return False, team
        else:
            return True, team
    else:
        # same as above + need to check if a piece from the king-in-check's team
        # can move into the path of the threatening piece.      
        # 1) Get path between threatening piece and king
        squares_between = get_between_exclusive(threatening_piece_pos, oppo_team_king_pos)
        # 2) Determine whether a piece can move into one of the squares between the threat and the king
        for target in squares_between:
            for piece in oppo_team.pieces:
                result = check_move(oppo_team, team, piece.pos, target, board)
                if result != 'illegal' and piece.type != 'king':
                    team.check = True
                    return False, team

    return True, team

def check_move(team, oppo_team, curr_pos, tar_pos, board):
    """
    The logic: check if move is illegal, if not determine
               whether it is a take or move action.
        Args:
            team: a Team object representing the team of the piece that is moving
            oppo_team: a Team object representing the opposing team of the piece that is moving
            curr_pos (str): the current board position of the piece that is moving (eg. 'a2')
            tar_pos (str): the square on the board that the piece is being moved to (eg. 'a4')
            board: a Board object containing the position of all pieces
    """
    colour = team.colour
    result = 'no_result'
    curr_x_y = [letter_to_number(curr_pos[0]), y_flip(curr_pos[1])]
    tar_x_y = [letter_to_number(tar_pos[0]), y_flip(tar_pos[1])]

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
        result = pawn_rules(colour, curr_pos, tar_pos, board)
    elif board.squares[curr_pos].type == 'rook':
        result = rook_rules(curr_pos, tar_pos)
    elif board.squares[curr_pos].type == 'knight':
        result = knight_rules(curr_pos, tar_pos)
    elif board.squares[curr_pos].type == 'bishop':
        result = bishop_rules(curr_pos, tar_pos)
    elif board.squares[curr_pos].type == 'king':
        result = king_rules(team, oppo_team, curr_pos, tar_pos, board)
    elif board.squares[curr_pos].type == 'queen':
        result = queen_rules(curr_pos, tar_pos)

    if result in ('kingside_castle', 'queenside_castle', 'illegal') :
        return result
    else:
        if not board.squares[tar_pos]:
            return 'move'
        else:
            return 'take'

def is_threatened(pos, oppo_team):
    """ Return True if given square is threatened by any piece in oppo_team
    """
    if pos in oppo_team.threatening:
        return True
    return False

def get_king_threat(pos):
    """ Return list of all squares threatened by the king
    """
    x = letter_to_number(pos[0])
    y = int(pos[1])
    threats = []
    

    dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    for pair in dirs:
        m = x + pair[0]
        n = y + pair[1]
        
        if m < 0 or m > 7 or n < 1 or n > 8:
            continue
        else:
            threats.append(number_to_letter(m) + str(n))
    return threats

def get_king_safe_moves(oppo_king_pos, team, squares):
    """ Returns list of squares the king can move to without being in check
    """
    safe_moves = []
    possible_moves = get_king_threat(oppo_king_pos)
    # print('possible moves: {}'.format(possible_moves))
    for square in possible_moves:
        if squares[square] == '':
            if square not in team.threatening:
                safe_moves.append(square)

    return safe_moves

def get_queen_threat(team, pos, squares):
    """ Return list of all squares threatened by the queen
    """
    diag_threats = get_diagonal_threat(team, pos, squares)
    x_threats = get_x_threat(team, pos, squares)
    y_threats = get_y_threat(team, pos, squares)

    return diag_threats + x_threats + y_threats

def get_diagonal_threat(team, pos, squares):
    dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    x = letter_to_number(pos[0])
    y = int(pos[1])
    threats = []

    for pair in dirs:
        m = x + pair[0]
        n = y + pair[1]
        while True:
            """ Continuously add pair to position until piece or edge encountered
            """
            if m < 0 or m > 7 or n < 1 or n > 8:
                # Edge encountered
                break
            else:
                if squares[number_to_letter(m) + str(n)]:
                    if squares[number_to_letter(m) + str(n)].team.colour == team.colour:
                        # Friendly piece encountered
                        threats.append(number_to_letter(m) + str(n))
                        break
                    elif squares[number_to_letter(m) + str(n)].team.colour != team.colour:
                        # Opponent piece encountered
                        threats.append(number_to_letter(m) + str(n))
                        break
                threats.append(number_to_letter(m) + str(n))
                    
                m = m + pair[0]
                n = n + pair[1]
    return threats

def get_L_threat(team, pos, squares):
    """ For knights
    """
    x = letter_to_number(pos[0])
    y = int(pos[1])
    threats = []
    
    dirs = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    for pair in dirs:
        m = x + pair[0]
        n = y + pair[1]

        if m < 0 or m > 7 or n < 1 or n > 8:
            continue  
        else:
            if squares[number_to_letter(m) + str(n)]:
                if squares[number_to_letter(m) + str(n)].team.colour == team.colour:
                    continue
            threats.append(number_to_letter(m) + str(n))

    return threats

def get_y_threat(team, pos, squares):
    """ return every square threatened in the y direction
        up to and including the first piece encountered.
    """
    y_threats = []

    for i in range(int(pos[1])+1, 9):
        """ Squares above
            int(pos[1])+1 because you don't threaten your own square
        """
        position = pos[0] + str(i)
        if squares[position] and squares[position].team.colour != team.colour:
            """ If first encountered taken square contains opponent, 
                add to threat and break
            """
            y_threats.append(position)
            break
        elif squares[position] and squares[position].team.colour == team.colour:
            """ If first encountered taken square contains ally,
                do not add to threat and break
            """
            y_threats.append(position)
            break
        y_threats.append(position)
    
    for i in range(int(pos[1])-1, 0, -1):
        """ Squares below
            int(pos[1])-1 because you don't threaten your own square
        """
        position = pos[0] + str(i)
        if squares[position] and squares[position].team.colour != team.colour:
            """ If first encountered taken square contains opponent, 
                add to threat and break
            """
            y_threats.append(position)
            break
        elif squares[position] and squares[position].team.colour == team.colour:
            """ If first encountered taken square contains ally,
                do not add to threat and break
            """
            y_threats.append(position)
            break
        y_threats.append(position)

    return y_threats 

def get_x_threat(team, pos, squares):
    """ return every square threatened in the x direction
        up to and including the first piece encountered.
    """
    x_threats = []

    for i in range(letter_to_number(pos[0])+1, 8):
        # get all squares to the right
        position = number_to_letter(i) + pos[1]
        if squares[position] and squares[position].team.colour != team.colour:
            """ If first encountered taken square contains opponent, 
                add to threat and break
            """
            x_threats.append(position)
            break
        elif squares[position] and squares[position].team.colour == team.colour:
            """ If first encountered taken square contains ally,
                do not add to threat and break
            """
            x_threats.append(position)
            break
        x_threats.append(position)
    for i in range(letter_to_number(pos[0])-1, -1, -1):
        # get all squares to the left
        position = number_to_letter(i) + pos[1]
        if squares[position] and squares[position].team.colour != team.colour:
            """ If first encountered taken square contains opponent, 
                add to threat and break
            """
            x_threats.append(position)
            break
        elif squares[position] and squares[position].team.colour == team.colour:
            """ If first encountered taken square contains ally,
                do not add to threat and break
            """
            x_threats.append(position)
            break
        x_threats.append(position)

    return x_threats

def update_team_threat(teams, board):
    """ this function needs to be called every time a piece is moved
    """
    for team in teams:
        for piece in team.pieces:
            # remove squares currently under threat
            team.remove_threat(piece.threatening)
            # add squares under threat after move
            piece.calculate_threat(board.squares)
            team.add_threat(piece.threatening)
    return teams

def get_between_exclusive(start, end):
    """ Return all squares between start and end exclusive
        y values = what the player sees (what's on side of board)

        Args
            start (str): a board position, eg. '12'
            end (str): a board position, eg. '42'
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

def get_x_between(exes):
    """
    EG. x1=a1, x2=d4
    returns [b2, c3]
    """
    x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    x1 = x.index(exes[0])
    x2 = x.index(exes[1])
    between = []
    if x1 > x2:
        temp = x1-1
        while temp >= x2:
            between.append(x[temp])
            temp -= 1
        return between
    elif x1 < x2:
        temp = x1+1
        while temp <= x2:
            between.append(x[temp])
            temp += 1
        return between
    else:
        return exes

def get_y_between(whys):
    between = []
    y1 = int(whys[0])
    y2 = int(whys[1])
    if y1 > y2:
        temp = y1-1
        while temp >= y2:
            between.append(temp)
            temp -= 1
        return between
    elif y1 < y2:
        temp = y1+1
        while temp <= y2:
            between.append(temp)
            temp += 1
        return between
    else:
        return whys

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

def letter_to_number_real(c):
    c = c.lower()
    if c == 'a':
        return 1
    elif c == 'b':
        return 2
    elif c == 'c':
        return 3
    elif c == 'd':
        return 4
    elif c == 'e':
        return 5
    elif c == 'f':
        return 6
    elif c == 'g':
        return 7
    elif c == 'h':
        return 8

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

def print_error(msg):
    print('ERROR:\n***\n{}\n***'.format(msg))

def get_piece_to_move():
    # required for testing
    return input('Piece to move: ')

def get_target_position():
    # required for testing
    return input('Move to: ')