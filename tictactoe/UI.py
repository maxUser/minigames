def welcome_message():
    print("""
            WELCOME
              TO
         TIC TAC TOE!!!
    """)

def print_symbol(symbol):
    if symbol == 'x':
        print("""
        """, end='')

def layout(choice_dict):
    # choice_dict = {board_position: value}
    for y in range(5):
        for x in range(5):
            if y == 0 and x == 0:
                print(choice_dict[0], end='')
            elif y == 0 and x == 1:
                print('||', end = '')
            elif y == 0 and x == 2:
                print(choice_dict[1], end='')
            elif y == 0 and x == 3:
                print('||', end = '')
            elif y == 0 and x == 4:
                print(choice_dict[2])
            elif y == 1 and x == 0:
                print('#######')
            elif y == 2 and x == 0:
                print(choice_dict[3], end='')
            elif y == 2 and x == 1:
                print('||', end = '')
            elif y == 2 and x == 2:
                print(choice_dict[4], end='')
            elif y == 2 and x == 3:
                print('||', end = '')
            elif y == 2 and x == 4:
                print(choice_dict[5])
            elif y == 3 and x == 0:
                print('#######')
            elif y == 4 and x == 0:
                print(choice_dict[6], end='')
            elif y == 4 and x == 1:
                print('||', end = '')
            elif y == 4 and x == 2:
                print(choice_dict[7], end='')
            elif y == 4 and x == 3:
                print('||', end = '')
            elif y == 4 and x == 4:
                print(choice_dict[8], '\n')

  #   print("""
  #   || ||
  # #########
  #   || ||O
  # #########
  #   || ||
  #   """)

#     print("""
#         ||      ||
#         ||      ||
#         ||      ||
# ###########################
#         ||      ||
#         ||      ||
#         ||      ||
# ###########################
#         ||      ||
#         ||      ||
#         ||      ||
#     """)
