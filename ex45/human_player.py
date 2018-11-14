from player import Player

class HumanPlayer(Player):
    def __init__(self, pos, sym):
        super(HumanPlayer, self).__init__(pos, sym)
        self.type = "Human"

    def choose_position(self, board):
        print "Choose an available position"
        return int(raw_input("> "))
