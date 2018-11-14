class Board(object):
    def __init__(self):
        self.positions = [None]*9

    def draw(self):
        for i in range(0, 3):
            print "\t\t %s | %s | %s " % (self.pos(i*3), self.pos(i*3+1), self.pos(i*3+2))
            if i < 2:
                print "\t\t-----------"

    def pos(self, pos):
        sym = str(pos)
        if self.positions[pos] != None:
            sym = self.positions[pos]

        return sym

    def is_position_empty(self, pos):
        return self.positions[pos] == None

    def fill_position(self, pos, symbol):
        self.positions[pos] = symbol

    def is_full(self):
        filtered = [p for p in self.positions if p == None]
        return len(filtered) == 0
