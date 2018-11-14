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

        game_over = True
        while game_over:
            self.board.draw()
            print "Player %d (%s - %s) turn:" % (self.current_player.pos, self.current_player.type, self.current_player.sym)
            pos = self.current_player.move(self.board)
            if not self.board.is_position_empty(pos):
                print "Position not avaliable. Try again!"
                continue

            self.board.fill_position(pos, self.current_player.sym)
            if self.is_winner(self.board, self.current_player.sym):
                game_over = False
                print "Player %d won!!!!" % self.current_player.pos
            elif self.board.is_full():
                game_over = False
                print "It's even!"
            else:
                self.change_player()

        self.board.draw()
        print "Game Over!"

    def change_player(self):
        if self.current_player.sym != self.player_1.sym:
            self.current_player = self.player_1
        else:
            self.current_player = self.player_2

    def is_winner(self, board, sym):
        if board.positions[0] == board.positions[1] == board.positions[2] == sym:
            return True

        if board.positions[3] == board.positions[4] == board.positions[5] == sym:
            return True

        if board.positions[6] == board.positions[7] == board.positions[8] == sym:
            return True

        if board.positions[0] == board.positions[3] == board.positions[6] == sym:
            return True

        if board.positions[1] == board.positions[4] == board.positions[5] == sym:
            return True

        if board.positions[2] == board.positions[5] == board.positions[8] == sym:
            return True

        if board.positions[0] == board.positions[4] == board.positions[8] == sym:
            return True

        if board.positions[2] == board.positions[4] == board.positions[6] == sym:
            return True

        return False

Game().start()
