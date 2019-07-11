from Card import Card

class Deck:

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ['Diamonds', 'Hearts', 'Spades', 'Clubs']:
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def printDeck(self):
        for card in self.cards:
            card.printCard()
