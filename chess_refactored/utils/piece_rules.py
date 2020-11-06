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

def bishop_rules(piece, target):
    from utils.helper import letter_to_number
    piece_x = letter_to_number(piece.pos[0])
    target_x = letter_to_number(target[0])
    piece_y = int(piece.pos[1])
    target_y = int(target[1])
    # Can only move diagonally
    if piece_x == target_x or piece_y == target_y:
        # disallow straight or lateral movement
        return False
    # disallow awkward moves like E3 to F5
    if abs(piece_x - target_x) - abs(piece_y - target_y) != 0:
        return False
    return True

def knight_rules(piece, target):
    """
        Knights can only move in an L shape.
        Ensure the tar_pos is +-2 x or y and
        +- 1 x or y.
        Example scenarios (White):
        1) Move up (y-2) and left (x-1)
        2) Move right (x+2) and up (y-1)
        3) Move down (y+2) and left (x-1)
        x operators are swapped for Black
    """
    from utils.helper import letter_to_number
    piece_x = letter_to_number(piece.pos[0])
    target_x = letter_to_number(target[0])
    piece_y = int(piece.pos[1])
    target_y = int(target[1])

    if abs(piece_x - target_x) == 1 and abs(piece_y - target_y) == 2:
        # up or down move
        return True
    elif abs(piece_y - target_y) == 1 and abs(piece_x - target_x) == 2:
        # lateral move
        return True
    else:
        return False

def rook_rules(piece, target):
    # Cannot move diagonally
    if piece.pos[0] != target[0] and piece.pos[1] != target[1]:
        return False
    return True

def pawn_rules(board, piece, target):
    # Cannot move backwards
    if piece.team.colour == 'white' and int(piece.pos[1]) > int(target[1]):
        return False
    elif piece.team.colour == 'black' and piece.pos[1] < target[1]:
        return False
    # Cannot move diagonally if no target piece
    if piece.pos[0] != target[0] and board.squares[target] is None:
        return False
    # Cannot move >2 squares
    if abs(int(piece.pos[1])-int(target[1])) > 2:
        return False
    # Cannot move >1 square if already moved
    if piece.moved is True and abs(int(piece.pos[1])-int(target[1])) > 1:
        return False
    # Cannot take piece straight ahead
    if piece.pos[0] == target[0] and board.squares[target] is not None:
        return False
    return True