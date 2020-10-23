# from utils.helper import letter_to_number, y_flip

def queen_rules(curr_pos, tar_pos):
    from utils.helper import letter_to_number, y_flip
    curr_x_y = [letter_to_number(curr_pos[0]), y_flip(curr_pos[1])]
    tar_x_y = [letter_to_number(tar_pos[0]), y_flip(tar_pos[1])]

    if curr_pos[0] != tar_pos[0] and curr_pos[1] != tar_pos[1]:
        # Non-straight movement
        if abs(curr_x_y[0] - tar_x_y[0]) - abs(curr_x_y[1] - tar_x_y[1]) != 0:
            # disallow awkward moves like E3 to F5
            return 'illegal'

    return None

def king_rules(team, oppo_team, curr_pos, tar_pos, board):
    from utils.helper import letter_to_number, y_flip, number_to_letter
    curr_x_y = [letter_to_number(curr_pos[0]), y_flip(curr_pos[1])]
    tar_x_y = [letter_to_number(tar_pos[0]), y_flip(tar_pos[1])]

    king = board.squares[curr_pos]
    if king.initial_pos is True:
        kingside_rook = board.squares[number_to_letter(curr_x_y[0]+3) + str(curr_pos[1])]
        queenside_rook = board.squares[number_to_letter(curr_x_y[0]-4) + str(curr_pos[1])]

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
    
    elif abs(curr_x_y[0] - tar_x_y[0]) > 1 or abs(curr_x_y[1] - tar_x_y[1]) > 1:
        # moving king more than 1 square
        return 'illegal'

    elif tar_pos in oppo_team.threatening:
        # king cannot move into check
        return 'illegal'
        

    return None

def bishop_rules(curr_pos, tar_pos):
    from utils.helper import letter_to_number, y_flip
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
    from utils.helper import letter_to_number, y_flip
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
    from utils.helper import letter_to_number, y_flip
    # Cannot move diagonally
    if curr_pos[0] != tar_pos[0] and curr_pos[1] != tar_pos[1]:
        return 'illegal'

    return None

def pawn_rules(colour, curr_pos, tar_pos, board):
    from utils.helper import letter_to_number, y_flip
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