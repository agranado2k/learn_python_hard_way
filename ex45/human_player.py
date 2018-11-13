from player import Player

class HumanPlayer(Player):
    def __init__(self, pos, sym):
        super(HumanPlayer, self).__init__(pos, sym)
        self.type = "Human"

    def choose_position(self):
        pass
