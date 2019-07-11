class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def printCard(self):
        if self.rank == 11:
            print('{} of {}'.format('Jack', self.suit))
        elif self.rank == 12:
            print('{} of {}'.format('Queen', self.suit))
        elif self.rank == 13:
            print('{} of {}'.format('King', self.suit))
        elif self.rank == 1:
            print('{} of {}'.format('Ace', self.suit))
        else:
            print('{} of {}'.format(self.rank, self.suit))
