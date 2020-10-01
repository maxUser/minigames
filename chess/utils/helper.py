def checkmate(team, oppo_team, squares):
    """ Determine whether oppo_team has been checkmated.
        A game position in which a player's king is in check 
        (threatened with capture) and there is no way to avoid the threat.

        Args
            team = the team that just played a move
            oppo_team = the other team (being checked)
            squares = dictionary of squares on the board and what they contain
    """
    oppo_team_king_pos = [piece.pos for piece in oppo_team.pieces if piece.type == 'king'][0]
    # Determine which piece is threatening the king
    threatening_piece = [piece for piece in team.pieces if oppo_team_king_pos in piece.threatening][0]
    # First, resolve check  
    if oppo_team_king_pos in team.threatening:
        print('{} is in check!'.format([piece for piece in team.pieces if piece.type == 'king'][0]))
        return 'check'
    else:
        return False
    # Second, resolve possible escape from check
    # 1) can the king move to a non-threatened square
    # 2) can a piece move into the path of the threat (non-knight, non-pawn threat)
    if threatening_piece.type not in ('knight', 'pawn'):
        # nothing can move into the path of the threat posed by knights or pawns
        pass

    print(get_king_threat(oppo_team, oppo_team_king_pos, squares))

    return False

def get_king_threat(team, pos, squares):
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
            break
        else:
            threats.append(number_to_letter(m) + str(n))
    return threats

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
            piece.calculate_threat(board.squares)
            for threat in piece.threatening:
                team.threatening.append(threat)
    return teams

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