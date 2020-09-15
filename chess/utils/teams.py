class Team:
    # still need algorithm to determine which squares a piece threatens given its current position.
    # store all squares threatened by a team here
    threatening = []


    def __init__(self, colour):
        self.colour = colour
        self.graveyard = []
