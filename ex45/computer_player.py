from player import Player

class ComputerPlayer(Player):
    def __init__(self, pos, sym):
        super(ComputerPlayer, self).__init__(pos, sym)
        self.type = "Computer"

    def choose_position(self):
        pass
