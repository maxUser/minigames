class Board:
    def __init__(self):
        self.positions = {0:'top left', 1:'top middle', 2:'top right',
                          3:'centre left', 4:'centre middle', 5:'centre right',
                          6:'bottom left', 7:'bottom middle', 8:'bottom right'}
        self.positions_taken = {0:' ', 1:' ', 2:' ',
                          3:' ', 4:' ', 5:' ',
                          6:' ', 7:' ', 8:' '}
