from human_player import HumanPlayer
from computer_player import ComputerPlayer
from board import Board

class Game(object):
    """
    The main game class
    """

    player_type = {
        "H": HumanPlayer,
        "C": ComputerPlayer
    }

    def start(self):
        """
        Setup the game
        Play the game
        """
        print "\tTic Tac Toe game."
        print "\t\tby agranad2k\n"

        self.setup()
        self.play()

    def setup(self):
        """
        set the players and board
        """
        self.set_players()
        self.board = Board()

    def set_players(self):
        print "Choose the players."
        p1_type = self.set_player_type(1)
        print "What is the player 1 symbol? X or O?"
        p1_sym = raw_input("> ")
        p2_type = self.set_player_type(2)
        p2_sym = self.invert_sym(p1_sym)
        self.player_1 = Game.player_type[p1_type](1, p1_sym)
        self.player_2 = Game.player_type[p2_type](2, p2_sym)
        self.player_1.describe()
        self.player_2.describe()

    def set_player_type(self, n):
        print "Is player %d Human (H) or Computer (C)?" % n
        return  raw_input("> ")

    def invert_sym(self, sym):
        if sym == "X":
            return "O"
        else:
            return "X"

    def play(self):
        """
        play the game
        """
        print "Let's play!!!"
        self.current_player = self.player_1

        self.board.draw()
        print "Player %d" % self.current_player.pos
        print "Choose an available position"
        pos = self.current_player.move()
        if not self.board.is_position_empty(pos):
            # repat the loop
            print "Position not avaliable. Try again!"
            # continue

        print "Marking pos %d" % pos
        self.board.fill_position(pos, self.current_player.sym)

        self.board.draw()

Game().start()
