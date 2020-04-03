class Player:
    # will contain array of companions
    def __init__(self, name):
        self.name = name

    def printPlayer(self):
        print('Name: {}'.format(self.name))
