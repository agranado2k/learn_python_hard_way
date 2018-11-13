class Player(object):
    def __init__(self, pos, sym):
        self.pos = pos
        self.sym = sym
        self.type = "Generic"

    def describe(self):
        print "Player %d is %s and has symbol %s" % (self.pos, self.type, self.sym)

    def move(self):
        return 0

    def choose_position(self):
        pass
