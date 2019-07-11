from Deck import Deck
from Player import Player
import random, sys

def calculateHandValue(player):
    # return value of player's hand
    return player.handValue()


def deal(deck):
    # return 2 random cards from Deck and remove them from Deck
    size = len(deck.cards)
    card1index = random.randint(1,size)
    card1 = deck.cards.pop(card1index)
    size = len(deck.cards)
    card2index = random.randint(1,size)
    card2 = deck.cards.pop(card2index)

    return [card1, card2]

def hit(player, deck):
    size = len(deck.cards)
    player.hand.append(deck.cards.pop(random.randint(1,size)))

def turn(player, deck):
    print('=======================')
    print('{} turn'.format(player.name))
    player.printPlayerHand()

    while True:
        total = calculateHandValue(player)
        if total > 21:
            break
        if total == 21:
            break
        print('------------------------')
        playerHit = input('Hit or Stay? (h/s): ')
        playerHit = playerHit.lower()
        if playerHit == 'stay' or playerHit == 's':
            print('{} turn is over'.format(player.name))
            break
        elif playerHit == 'hit' or playerHit == 'h':
            hit(player, deck)
        player.printPlayerHand()


def main():
    deck = Deck()
    p1 = Player('PLAYER 1')
    p1.hand = deal(deck)
    p2 = Player('DEALER')
    p2.hand = deal(deck)


    turn(p1, deck)
    p1total = calculateHandValue(p1)
    if p1total > 21:
        print('you broke 21 - Player 2 Wins!')
        sys.exit()
    elif p1total == 21:
        print('you have 21 - Player 1 Wins!')
        sys.exit()

    turn(p2, deck)
    p2total = calculateHandValue(p2)
    if p2total > 21:
        print('you broke 21 - Player 1 Wins!')
        sys.exit()

    if p2total == 21:
        print('you have 21 - {} Wins!'.format(p2.name))
    elif p1total > p2total and p1total < 21:
        print('{} Wins!'.format(p1.name))
    elif p1total < p2total and p2total < 21:
        print('{} Wins!'.format(p2.name))
    elif p1total == p2total and p1total < 21 and p2total < 21:
        print('Tie!')
        print('Dealer Wins!')
    else:
        print('what heppened?')



if __name__ == "__main__":
    main()
