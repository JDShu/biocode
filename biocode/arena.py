from collections import deque

class Arena:

    def __init__(self, width, length):
        self.w, self.length = width, length
        self.map = [[None]*self.w for i in xrange(length)]
        self.creatures = deque()
        self.finished = False
        
    def update(self):
        for c in self.creatures:
            self.place_creature(None, (c.pos_x,c.pos_y))
            c.update()
            self.place_creature(c, (c.pos_x,c.pos_y))
            
    def add_creature(self, creature, pos):
        creature.set_pos(pos)
        self.creatures.append(creature)
        self.place_creature(creature, pos)
        
    def place_creature(self, creature, pos):
        self.map[pos[0]][pos[1]] = creature
