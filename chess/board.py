from termcolor import colored


class Board:
    board = [
                ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
                ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
            ]

    def square(self, pos):
        # print(pos)
        return self.board[pos[1]][pos[0]]


    def alter(self, old_pos, new_pos):
        piece = self.board[old_pos[1]][old_pos[0]]
        print(self.board[old_pos[0]][old_pos[1]])
        self.board[old_pos[1]][old_pos[0]] = ' '
        self.board[new_pos[1]][new_pos[0]] = piece


    def print(self):
        x_axis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        y_axis = ['8', '7', '6', '5', '4', '3', '2', '1']
        # white = lower case
        # black = upper case

        print('  ===================================')

        axis_count = 0
        for row in self.board:
            print(y_axis[axis_count]+' ||', end=' ')
            last_col = 0
            for square in row:
                if square.isupper():
                    print(colored(square, 'yellow'), end=' ')
                else:
                    print(colored(square, 'red'), end=' ')
                if last_col == 7:
                    print('||')
                else:
                    print('|', end=' ')
                last_col += 1


            if axis_count == 7:
                print('  ===================================')
            else:
                print('  -----------------------------------')
            axis_count += 1

        for x in x_axis:
            if x == 'a':
                print('     '+x, end=' ')
            else:
                print('  '+x, end=' ')
        print()
