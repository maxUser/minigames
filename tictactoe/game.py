from Player import Player
from Board import Board

win_conditions = [set([0, 1, 2]), set([0, 4, 9]), set([0, 3, 6]),
                      set([1, 4, 7]), set([1, 4, 7]), set([2, 5, 9]),
                      set([2, 4, 6]), set([3, 4, 5]), set([6, 7, 9])]

def check_win(pos_list):
    pos_set = set(pos_list)
    for win_set in win_conditions:
        if pos_set.issuperset(win_set):
            print(win_set)
            print('win_set in pos_set')
            return 1
    return None

def turn(player, board):
    print(player.name + '\'s turn')
    for key, value in board.positions.items() :
        print(str(key) + ') ' + value)

    pos = input('Pick a number corresponding to a board position: ')

    player.positions_chosen.append(int(pos))
    board.positions[(int(pos))] = '------------'
    winner = check_win(player.positions_chosen)
    if winner == 1:
        return player


def game(p1, p2):
    board = Board()
    count = 0
    winner = None
    while True:
        print('Turn: ' + str(count+1))

        if count % 2 == 0:
            winner = turn(p1, board)
        else:
            winner = turn(p2, board)

        if winner != None:
            return winner

        count = count + 1

def main():
    # p1_name = input('Player 1 name: ')
    # p2_name = input('Player 2 name: ')
    p1_name = 'maxi'
    p2_name = 'mikey'
    p1 = Player(p1_name)
    p2 = Player(p2_name)

    winner = game(p1, p2)
    print(winner.name + ' wins! Congratulations!')

if __name__ == '__main__':
    main()
