class Player:
    def __init__(self, name):
        self.hand = [] # list of cards
        self.name = name

    def printPlayerHand(self):
        for card in self.hand:
            card.printCard()

    def handValue(self):
        value = 0
        ace = False
        ten = False
        for card in self.hand:
            if card.rank > 10:
                value += 10
                ten = True
            else:
                value += card.rank
                if card.rank == 1:
                    ace = True
        if ace is True and ten is True and len(self.hand) == 2:
            return 21
        elif ace is True and (value+10) < 21:
            # ace has value of 11 as long as it doesn't break 21
            value += 10

        return value
