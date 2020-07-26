class Piece:
    pos = [-1, -1]

    def move(self, new_pos):
        # TODO: check if new_pos is valid move
        self.pos[0] = new_pos[0]
        self.pos[1] = new_pos[1]

    def __str__(self):
        return self.team + ' ' + self.type + ' at ' + str(self.pos[0]) + ', ' + str(self.pos[1])

    def __init__(self, type, team, starting_pos):
        self.type = type
        self.team = team
        self.pos = starting_pos
