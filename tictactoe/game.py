from Player import Player
from Board import Board
from UI import welcome_message, layout

win_conditions = [set([0, 1, 2]), set([0, 4, 9]), set([0, 3, 6]),
                      set([1, 4, 7]), set([1, 4, 7]), set([2, 5, 8]),
                      set([2, 4, 6]), set([3, 4, 5]), set([6, 7, 8])]

def check_win(pos_list):
    pos_set = set(pos_list)
    for win_set in win_conditions:
        if pos_set.issuperset(win_set):
            # print(win_set)
            return 1
    return None

def turn(player, board):
    print(player.name + '\'s turn')
    for key, value in board.positions.items() :
        print(str(key) + ') ' + value)

    pos = input(player.name + ', pick a number: ')

    if board.positions[(int(pos))] == 'X' or board.positions[(int(pos))] == 'O':
        for i in range(20):
            print('')
        print('That position has already been picked.\nPlease pick another!')
        turn(player, board)

    player.positions_chosen.append(int(pos))
    if player.num == 0:
        board.positions[(int(pos))] = 'X'
        board.positions_taken[(int(pos))] = 'X'
    elif player.num == 1:
        board.positions[(int(pos))] = 'O'
        board.positions_taken[(int(pos))] = 'O'
    winner = check_win(player.positions_chosen)
    if winner == 1:
        return player


def game(p1, p2, board):

    count = 0
    winner = None
    while True:
        if count > 0:
            for i in range(20):
                print('')
        print('Turn: ' + str(count+1))
        layout(board.positions_taken)
        if count % 2 == 0:
            winner = turn(p1, board)
        else:
            winner = turn(p2, board)

        if winner != None:
            return winner

        count = count + 1

def main():
    welcome_message()
    # p1_name = input('Player 1 name: ')
    # p2_name = input('Player 2 name: ')

    p1_name = 'maxi'
    p2_name = 'mikey'
    p1 = Player(p1_name, 0)
    p2 = Player(p2_name, 1)
    board = Board()

    winner = game(p1, p2, board)
    layout(board.positions_taken)
    print(winner.name + ' wins! Congratulations!')

if __name__ == '__main__':
    main()
