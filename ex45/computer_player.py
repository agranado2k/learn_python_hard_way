from player import Player

import random

class ComputerPlayer(Player):
    def __init__(self, pos, sym):
        super(ComputerPlayer, self).__init__(pos, sym)
        self.type = "Computer"

    def choose_position(self, board):
        while True:
            pos = random.randint(0, len(board.positions) -1)
            if board.is_position_empty(pos):
                return pos
