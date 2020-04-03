'''
ROULETTE

required:
    -randomizer to simulate wheel (european layout: http://www.fouroulette.com/roulette-wheel.htm)
    -betting options
        -print message that wheel is spinning ('place your bets')
        -wait 5 seconds
        -'no more bets'
        -wait 5 seconds, show result
    -betting amount
    -players
    -player totals
'''

class Player:

    def __init__(self, name):
        self.name = name
        self.money = 100
        self.bets = []

    def add_bet(bet):
        self.bets.append(bet)

    def gain_money(amount):
        self.money = self.money + amount

    def lose_money(amount):
        self.money = self.money - amount


# spin_wheel()
# return a number/colour pair
# colour/number pairs must be hardcoded
def spin_wheel(wheel):
    import random
    num = random.randint(0, 36)
    return (num, wheel[num])


# init_wheel()
# return a dictionary of number/colour pairs
def init_wheel():
    wheel = {
        0: 'green',
        1: 'red',
        2: 'black',
        3: 'red',
        4: 'black',
        5: 'red',
        6: 'black',
        7: 'red',
        8: 'black',
        9: 'red',
        10: 'black',
        11: 'black',
        12: 'red',
        13: 'black',
        14: 'red',
        15: 'black',
        16: 'red',
        17: 'black',
        18: 'red',
        19: 'red',
        20: 'black',
        21: 'red',
        22: 'black',
        23: 'red',
        24: 'black',
        25: 'red',
        26: 'black',
        27: 'red',
        28: 'black',
        29: 'black',
        30: 'red',
        31: 'black',
        32: 'red',
        33: 'black',
        34: 'red',
        35: 'black',
        36: 'red'
    }
    return wheel


def bet_table():
    # square_thirds
    # line_thirds
    # 1st/2nd half
    # red/black
    # odd/even
    # individual numbers



def make_bet(player):
    return 0



def main():
    wheel = init_wheel()
    print(spin_wheel(wheel))


if __name__ == '__main__':
    main()
